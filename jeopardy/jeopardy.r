##Values double on Ep. 3966, November 26, 2001
#Import/prepare score data
setwd("c:/Users/David/Documents/NYCDSA/Project 2/score")
jeop_score<-read.csv("Jeopardy_score.csv", stringsAsFactors = F)
jeop_score<-jeop_score[, c("Episode", "Date", "Contestant", "Comment", "ScoreFirst", "ScoreSecond", "FinalCat", "FinalQ", "FinalA", "FinalCorrect", "Final")]
jeop_score$ScoreFirst<-as.numeric(jeop_score$ScoreFirst)
jeop_score$ScoreSecond<-as.numeric(jeop_score$ScoreSecond)
jeop_score$Final<-as.numeric(jeop_score$Final)
jeop_score$Date<-gsub(".*day, ", "", jeop_score$Date)
jeop_score$Date<-as.Date(jeop_score$Date, "%B %d, %Y")
  


library(dplyr)
jeop_score_plus<- jeop_score %>% mutate(Wager = abs(Final - ScoreSecond), SecondOnly = ScoreSecond - ScoreFirst)

#What percentage of Jeopardy/Double Jeopardy Leaders win the game?  How much does each Round add, on average, to the winner's win probability?

winners<-jeop_score_plus %>% group_by(Episode) %>% filter(Final==max(Final)) %>% select(Episode, Date, Contestant, Final)
dj.leader<-jeop_score_plus %>% group_by(Episode) %>% filter(ScoreSecond==max(ScoreSecond)) %>% select(Episode, Contestant, ScoreSecond)
j.leader<-jeop_score_plus %>% group_by(Episode) %>% filter(ScoreFirst==max(ScoreFirst)) %>% select(Episode, Contestant, ScoreFirst)

losers<-jeop_score_plus %>% group_by(Episode) %>% filter(Final==min(Final)) %>% select(Episode, Date, Contestant, Final)
dj.loser<-jeop_score_plus %>% group_by(Episode) %>% filter(ScoreSecond==min(ScoreSecond)) %>% select(Episode, Contestant, ScoreSecond)
j.loser<-jeop_score_plus %>% group_by(Episode) %>% filter(ScoreFirst==min(ScoreFirst)) %>% select(Episode, Contestant, ScoreFirst)

win.dj<-full_join(dj.leader, winners, by= "Episode")
win.j<-full_join(j.leader, winners, by= "Episode")
same.dj.win<-win.dj %>% filter(Contestant.x==Contestant.y)
same.j.win<-win.j %>% filter(Contestant.x==Contestant.y)

lose.dj<-full_join(dj.loser, winners, by="Episode")
lose.j<-full_join(j.loser, winners, by="Episode")
diff.dj.win<-lose.dj %>% filter(Contestant.x==Contestant.y)
diff.j.win<-lose.j %>% filter(Contestant.x==Contestant.y)

comp.games<-length(unique(winners$Episode))
second.prob<-c(nrow(same.dj.win)/comp.games, (comp.games - nrow(same.dj.win) - nrow(diff.dj.win))/comp.games, nrow(diff.dj.win)/comp.games)
first.prob<-c(nrow(same.j.win)/comp.games, (comp.games - nrow(same.j.win) - nrow(diff.j.win))/comp.games, nrow(diff.j.win)/comp.games)

#Plot it
library(ggplot2)
library(ggthemes)
win.prob<-c(first.prob, second.prob)
round<-c("Jeopardy!", "Jeopardy!", "Jeopardy!", "Double Jeopardy!","Double Jeopardy!","Double Jeopardy!")
place<-c("1st", "2nd", "3rd", "1st", "2nd", "3rd")
prob.graph<-data.frame(round, place, win.prob)
colnames (prob.graph)= c("Round", "Place", "Win.Probability")
prob.graph$Round<-factor(prob.graph$Round, levels=c("Jeopardy!", "Double Jeopardy!"))
j<-ggplot(data=prob.graph, aes(x=Place, y=Win.Probability))
j + geom_bar(stat="identity", aes(fill=Place)) + facet_grid(.~ Round) + labs(title="Probability of Winning Based on Position After Each Round", y="Win Probability") +  geom_label(label=paste0(signif(prob.graph$Win.Probability * 100, 3), "%")) + theme_economist() + guides(fill=F) + theme(plot.title = element_text(hjust = 0.5)) + scale_fill_manual(values=c("darkblue", "steelblue1", "blue"))

prob.added<-data.frame(c("Jeopardy!", "Double Jeopardy!", "Final Jeopardy!"), c(nrow(same.j.win)/comp.games- 1/3, nrow(same.dj.win)/comp.games - nrow(same.j.win)/comp.games, 1 - nrow(same.dj.win)/comp.games))
colnames (prob.added)= c("Round", "Win.Probability.Added")
prob.added$Round<-factor(prob.added$Round, levels=c("Jeopardy!", "Double Jeopardy!", "Final Jeopardy!"))
wpa<-ggplot(data=prob.added, aes(x=Round, y=Win.Probability.Added))
wpa + geom_bar(stat="identity", aes(fill=Round)) + labs(title="Average Winner's WPA (Win Probability Added) by Round", y = "Win Probability Added") + geom_label(label=paste0(signif(prob.added$Win.Probability.Added * 100, 3), "%")) + theme_economist() + guides(fill=F) + theme(plot.title = element_text(hjust = 0.5)) + scale_fill_manual(values=c("darkblue", "steelblue1", "blue"))

#How well does performance in each round predict performance in following rounds?
jeop_plus<-jeop_score_plus[complete.cases(jeop_score_plus),]
r<-cor.test(jeop_plus$ScoreFirst, jeop_plus$SecondOnly) #r=.39, p < 2x10e-16
jeop_model<-lm(jeop_plus$SecondOnly ~ jeop_plus$ScoreFirst)
skill<-ggplot(data=jeop_plus, aes(x=ScoreFirst, y=SecondOnly))
skill + geom_point(aes(color=jeop_plus$FinalCorrect)) + geom_smooth(method="lm", color="black") + labs(title= "Comparing Jeopardy! Round Performances", x="Jeopardy! Score ($)", y="Double Jeopardy! Score ($)", color="Correct Final Jeopardy! Answer") +  theme_economist() + theme(legend.position = "right", plot.title = element_text(hjust = 0.5)) + geom_text(x=-1000, y=35000, label=paste0("y = ", round(jeop_model$coefficients[1]), " + ", signif(jeop_model$coefficients[2], 3), "x, r = ", signif(r[[4]][[1]],2), ", p < 2.2e-16"))

library(VIM)
jeop_final<-jeop_plus[jeop_plus$ScoreSecond>0,]
final.right<-jeop_final %>% group_by(FinalCorrect) %>% summarize(Percent=n()/nrow(jeop_final)) #50.7% wrong, 49.2% right

set.seed(5)
train<-sample(1:nrow(jeop_final), .3*nrow(jeop_final))
jeop_test<-jeop_final
jeop_test[train, "FinalCorrect"]<-NA
imputed<-kNN(jeop_test, variable="FinalCorrect", dist_var = "ScoreSecond", 126)  
final.predict<-table(imputed$FinalCorrect[train], jeop_final$FinalCorrect[train])#Correct only 50.4% of the time!
final.knn<-data.frame(c("Correct", "Incorrect"), c((final.predict[1,1]+final.predict[2,2])/length(train), (final.predict[1,2]+final.predict[2,1])/length(train)))
colnames(final.knn)<-c("kNN.Result", "Percentage")

fj1<-ggplot(data=final.right, aes(x = factor(1), y=Percent, fill=FinalCorrect))
fj1 + geom_bar(stat="identity", position="fill") + coord_polar(theta="y") + labs(title="Correct Final Jeopardy! Responses, All Contestants", x="", y="Percentage Correct", fill="Correct?") + geom_label(label=paste(signif(final.right$Percent, 3)*100, "%"), position="jitter")

fj2<-ggplot(data = final.knn, aes(x=factor(1), y=Percentage, fill=kNN.Result))
fj2 + geom_bar(stat="identity", position="fill") + coord_polar(theta="y") + labs(title="Accurate kNN Prediction of Final Jeopardy! Answer from Jeopardy!/Double Jeopardy! Score", x="", y="Percentage Correct", fill="kNN Model (k=15)") + geom_label(label=paste(signif(final.knn$Percentage, 3)*100, "%"), position="jitter")

#What are the most common final answers?

answers<-jeop_score %>% group_by(FinalA) %>% summarize(Total = ceiling(n()/3))
categories<-jeop_score %>% group_by(FinalCat) %>% summarize(Total = ceiling(n()/3))
answers<-answers[order(answers$Total, decreasing=T),]
categories<-categories[order(categories$Total, decreasing=T),]


#Who are the biggest winners in show history?

winnings<-winners %>% group_by(Contestant) %>% summarize(Total = sum(Final), Start = min(Date))
winnings<-winnings[order(winnings$Total, decreasing=T), ]
plot(winnings$Start, winnings$Total)

#Fun with outliers

filter(winners, Final==min(Final))
#2 (trick question--20th c), #3190 (two tied, one out, DAR), #7216 (two tied, Little Rock) had no winner--plus three Celebrity games where everyone tied(Teri Garr, Naomi Judd, Jane Curtin; Matthew Fox, Jon Lovitz, Carl Lewis; Kelton Ellis, Joe Vertnik, Tori Amos)
real.winners <- winners[winners$Final>0, ] 
filter(real.winners, Final==min(Final))
#$1 winner Darryl Scott--everyone whiffed on Mandela; Ben Salisbury and Brandi Chastain in Celebs

#The Questions
setwd("c:/Users/David/Documents/NYCDSA/Project 2/jeopardy_1")
jeop_qs<-read.csv("Jeopardy.csv", stringsAsFactors=F)
jeop_qs<-jeop_qs[, c("Episode", "Date", "Round", "Order", "Category", "Value", "Clue", "Answer", "Right", "Wrong1", "Wrong2", "Wrong3", "Wrong4", "DailyDouble")]
jeop_qs$Value<-as.numeric(jeop_qs$Value)
jeop_qs$DailyDouble<-as.numeric(jeop_qs$DailyDouble)
jeop_qs$Date<-gsub(".*day, ", "", jeop_qs$Date)
jeop_qs$Date<-as.Date(jeop_qs$Date, "%B %d, %Y")

#How many questions go unasked?

nrow(jeop_qs[jeop_qs$Clue=="Not asked",])/nrow(jeop_qs)


#debug
jeop_score %>% group_by(Date) %>% summarize(Number = n()) %>% filter(Number!=3)
error1<-jeop_qs$Episode[!(jeop_qs$Episode %in% jeop_score$Episode)]
error1<-unique(error1)
debug<-jeop_qs %>% group_by(Date) %>% summarize(TotalQ = n())
error2<-filter(debug, TotalQ!=60)


#Uninteresting stuff
#Have contestants won more over time?
winners1<-filter(winners, Date >= as.Date("November 26, 2001", "%B %d, %Y"))
winners2<-filter(winners, Date < as.Date("November 26, 2001", "%B %d, %Y"))
hist(winners1$Final, breaks=20)
hist(winners2$Final, breaks=20)

plot(winners$Date, winners$Final)
