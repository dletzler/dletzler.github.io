Commercial# Clean very, very dirty set

import fnmatch
import re

lists_final['publisher'] = lists_final['publisher'].replace("PUNAM", "PUTNAM", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("PENGUN", "PENGUIN", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("MULHOLLAND", "MULLHOLLAND", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("^ALLANTINE", "BALLANTINE", regex=True)

lists_final['publisher'] = lists_final['publisher'].str.upper()
lists_final['publisher'] = lists_final['publisher'].replace("’", "''", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("''", "'", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" PRESS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" GROUP$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" HOUSE$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" PUBLISHING$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" PUBLISHERS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" BOOKS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" ROMANCE$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(",$", "", regex=True)

lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("SOURCEBOOKS*"), "SOURCEBOOKS", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/HARPERCOLLINS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/HARPER COLLINS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/WILLIAM MORROW$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/SIMON & SCHUSTER$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/RANDOM HOUSE$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/LITTLE, BROWN$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/HOUGHTON MIFFLIN$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/HOUGHTON MIFFLIN HARCOURT$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/HARCOURT$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/GRAND CENTRAL$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/GROVE$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/SCOUT$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/VIKING$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/TOM DOHERTY$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/KENSINGTON$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/MERCURY RADIO ARTS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(" EDITIONS$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(", INC.$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("BERKELEY", "BERKLEY", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/HOLT$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/PUTNAM$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/DOUBLEDAY$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/ST. MARTIN'S$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/ATRIA$", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("\/FARRAR, STRAUS & GIROUX$", "", regex=True)

lists_final['publisher'] = lists_final['publisher'].replace("^KNOPF/", "", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("HARLEQUIN MIRA", "MIRA", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("WILLIAM MORROW", "MORROW", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("PENGUIN*"), "PENGUIN", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") + fnmatch.translate("LITTLE*"), "LITTLE, BROWN", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("HOUGHTON MIFFLIN*"), "HOUGHTON MIFFLIN HARCOURT", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*HQN") + str("$"), "HQN", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("HARLEQUIN*"), "HARLEQUIN", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("HENRY HOLT*"), "HOLT", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("GRAND CENTRAL*"), "GRAND CENTRAL", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("VIKING*"), "VIKING", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("HOGARTH*"), "HOGARTH", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("BLOOMSBURY*"), "BLOOMSBURY", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("REAGAN ARTHUR*"), "REAGAN ARTHUR", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("EMILY BESTLER*"), "EMILY BESTLER", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*EMILY BESTLER*") + str("$") , "EMILY BESTLER", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("SIGNET*"), "SIGNET", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("NAL*"), "NEW AMERICAN LIBRARY", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("NAN A. TALESE*"), "NAN A. TALESE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("NAN. A TALESE", "NAN A. TALESE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("VOICE*"), "VOICE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("CREATESPACE*"), "CREATESPACE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("NORTON*"), "W. W. NORTON", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("LUCAS*"), "LUCASBOOKS", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*PERENNIAL") + str("$"), "PERENNIAL", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*VOYAGER") + str("$"), "VOYAGER", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*FORGE") + str("$"), "FORGE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*MACRAE") + str("$"), "JOHN MACRAE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*MINOTAUR") + str("$"), "MINOTAUR", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*ENTANGLED*"), "ENTANGLED", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*PUTNAM*"), "PUTNAM", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*H.*M.*"), "H.M. WARD", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(fnmatch.translate("*DOHERTY*"), "TOR", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("WARNER", "GRAND CENTRAL", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("TOM DOHERTY ASSOCIATES", "TOR", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("EL LE*"), "EL LEON LITERARY ARTS", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("BANTAM*"), "BANTAM", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("DEL REY*"), "DEL REY", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("DELL*"), "DELL", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("CROWN*"), "CROWN", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("TOR*"), "TOR", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("ST.*"), "ST. MARTIN'S", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("ZEBRA*"), "ZEBRA", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("KNOPF DOUBLEDAY", "DOUBLEDAY", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("HACHETTE", "HYPERION", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace('ELLORA"S CAVE', "ELLORA'S CAVE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace("MARION WOOD", "MARIAN WOOD", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("HARPER") +str("$"), "HARPERCOLLINS", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("HARPER/*"), "HARPERCOLLINS", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace(str("^") +fnmatch.translate("THOMAS DUNNE*"), "THOMAS DUNNE", regex=True)
lists_final['publisher'] = lists_final['publisher'].replace('DOUBLE\xc2\xadDAY', "DOUBLEDAY", regex=True)

#Associate imprints with corporate parent company

corp_owner = { "Grand Central": "Hachette",
                "Bantam" : "Random House",
                "Berkley": "Penguin",
                "Little, Brown": "Hachette",
                "Putnam" : "Penguin",
                "Vintage": "Random House",
                "Ballantine": "Random House",
                "Scribner": "Simon & Schuster",
                "Dell": "Random House",
                "Broadway": "Random House",
                "Riverhead": "Penguin",
                "Morrow": "HarperCollins",
                "Penguin": "Penguin",
                "Vision": "Hachette",
                "Random" : "Random House",
                "Knopf" : "Random House",
                "Simon & Schuster" : "Simon & Schuster",
                "Doubleday" : "Random House",
                "St. Martin's" : "Macmillan",
                "Jove" : "Penguin",
                "Signet" : "Penguin",
                "Delacorte" : "Random House",
                "Pocket" : "Simon & Schuster",
                "Harlequin" : "HarperCollins",
                "Dutton": "Penguin",
                "Anchor" : "Random House",
                "Crown": "Random House",
                "Mira" : "HarperCollins",
                "Back Bay" : "Hachette",
                "Ace" : "Penguin",
                "Washington Square": "Simon & Schuster",
                "Perennial": "HarperCollins",
                "Viking": "Penguin",
                "Atria" : "Simon & Schuster",
                "Amy Einhorn" : "Penguin",
                "HarperOne" : "HarperCollins",
                "Vintage Crime/Black Lizard" : "Random House",
                "Kensington" : "Independent",
                "Tor" : "Macmillan",
                "Emily Bestler" : "Simon & Schuster",
                "Gallery" : "Simon & Schuster",
                "Windblown Media" : "Independent",
                "Avon": "HarperCollins",
                "Picador": "Macmillan",
                "Frontline" : "Independent",
                "Algonquin" : "Independent",
                "St. Martin's Griffin" : "Macmillan",
                "Del Rey" : "Random House",
                "Plume" : "Penguin",
                "Silhouette" : "HarperCollins",
                "Farrar, Straus & Giroux": "Macmillan",
                "Pamela Dorman" : "Penguin",
                "Vintage International": "Random House",
                "Europa" : "Independent",
                "Hyperion" : "Hachette",
                "Touchstone" : "Simon & Schuster",
                "Grove" : "Grove/Atlantic",
                "Roc" : "Penguin",
                "Pocket Star" : "Simon & Schuster",
                "Ecco" : "HarperCollins",
                "Scout" : "Simon & Schuster",
                "Andrews McMeel" : "Independent",
                "Marian Wood" : "Penguin",
                "HarperCollins" : "HarperCollins",
                "Three Rivers" : "Random House",
                "Vintage Contemporaries" : "Random House",
                "Harper Paperbacks" : "HarperCollins",
                "Pantheon" : "Random House",
                "Entangled" : "Independent",
                "Free" : "Simon & Schuster",
                "Hard Case Crime" : "Independent",
                "Forever" : "Hachette",
                "Forge" : "Macmillan",
                "Howard": "Simon & Schuster",
                "Hogarth" : "Random House",
                "Deborah Bladon": "Self-published",
                "Sarah Crichton": "Macmillan",
                "Colleen Hoover" : "Self-published",
                "Mariner" : "Houghton Mifflin Harcourt",
                "DAW" : "Penguin",
                "Flatiron" : "Macmillan",
                "Waterhouse" : "Independent",
                "Barbara Freethy" : "Self-published",
                "Berkley Sensation" : "Penguin",
                "Wizards of the Coast" : "Hasbro",
                "New American Library" : "Penguin",
                "BookShots" : "Hachette",
                "Quirk" : "Independent",
                "Helen Cooper" : "Self-published",
                "Threshold" : "Simon & Schuster",
                "Lauren Blakely" : "Self-published",
                "Delta" : "Random House",
                "Orbit" : "Hachette",
                "Jessica Sorensen" : "Self-published",
                "Reagan Arthur" : "Hachette",
                "Nan A. Talese" : "Random House",
                "Spiegel & Grau" : "Random House",
                "Tyndale" : "Independent",
                "J.C. Reed": "Self-published",
                "Laree Bailey" : "Independent",
                "LucasBooks" : "Random House",
                "Center Street" : "Hachette",
                "Bethany" : "Independent",
                "Abbi Glines" : "Self-published",
                "Thomas Nelson" : "HarperCollins",
                "FaithWords" : "Hachette",
                "Holt" : "Macmillan",
                "Witness Impulse" : "HarperCollins",
                "John Macrae" : "Macmillan",
                "Mullholland" : "Hachette",
                "Zondervan" : "HarperCollins",
                "HTJB" : "Penguin",
                "Jamie McGuire" : "Self-published",
                "InterMix" : "Penguin",
                "Rachel Van Dyken" : "Self-published",
                "Houghton Mifflin Harcourt" : "Houghton Mifflin Harcourt",
                "Darcie Chan": "Self-published",
                "Zebra" : "Kensington",
                "Pinnacle" : "Kensington",
                "Vi Keeland" : "Self-published",
                "Tracey Garvis-Graves" : "Self-published",
                "Atlantic Monthly" : "Grove/Atlantic",
                "Kristen Ashley" : "Self-published",
                "Oak" : "Independent",
                "Laurelin Paige" : "Self-published",
                "Gail McHugh" : "Self-published",
                "Kendall Ryan" : "Self-published",
                "Baen" : "Independent",
                "Penelope Ward" : "Self-published",
                "Berkley Prime Crime" : "Penguin",
                "Voyager" : "HarperCollins",
                "Samhain" : "Independent",
                "Liveright" : "W. W. Norton",
                "Putnam Adult" : "Penguin",
                "Loveswept" : "Random House",
                "Tijan" : "Self-published",
                "Sourcebooks" : "Independent",
                "Soho" : "Independent",
                "Jasinda Wilder" : "Self-published",
                "Thomas Dunne" : "Macmillan",
                "Ellora's Cave" : "Independent",
                "McSweeney's": "Random House",
                "Denise Grover Swank" : "Self-published",
                "Del Rey" : "Random House",
                "Gossamer" : "Independent",
                "Ampersand" : "Independent",
                "Harvest" : "Houghton Mifflin Harcourt",
                "M. Leighton" : "Self-published",
                "EverAfter" : "Independent",
                "Rutherford" : "Self-published",
                "Metal Blonde" : "Independent",
                "Aurora Rose Reynolds" : "Self-published",
                "J.A. Redmerski" : "Self-published",
                "Catherine Bybee" : "Self-published",
                "H.M. Ward" : "Self-published",
                "Kingswell" : "Hachette",
                "Lisa Renee Jones" : "Self-published",
                "Addison Moore" : "Self-published",
                "Obsidian" : "Penguin",
                "DLZ Entertainment" : "Independent",
                "Eos": "HarperCollins",
                "Brava" : "Kensington",
                "Avon Impulse" : "HarperCollins",
                "Grove/Atlantic" : "Grove/Atlantic",
                "Black Cat" : "Grove/Atlantic",
                "W. W. Norton": "W. W. Norton",
                "Morrow Impulse" : "HarperCollins",
                "Bloomsbury" : "Independent",
                "HQN" : "HarperCollins",
                "Dial" : "Random House",
                "Bellevue Literary" : "Independent",
                "Minotaur" : "Macmillan",
                "Michael Prescott" : "Self-published",
                "Chris Culver" : "Self-published",
                "Overlook" : "Independent",
                "Voice" : "Hachette",
                "Dorchester" : "Independent",
                "Stephanie McAfee" : "Self-published",
                "Penwyck" : "Independent",
                "Legacy" : "Independent",
                "Shaye Areheart" : "Random House",
                "NAL Accent" : "Random House",
                "El Leon Literary Arts" : "Grove/Atlantic",
                "CreateSpace" : "Self-published",
                "Rerum" : "Independent"
}

#Associate imprint with genre

genre = { "Grand Central": "Commercial",
                "Bantam" : "Genre",
                "Berkley": "Genre",
                "Little, Brown": "Commercial",
                "Putnam" : "Commercial",
                "Vintage": "Commercial",
                "Ballantine": "Commercial",
                "Scribner": "Literary",
                "Dell": "Genre",
                "Broadway": "Commercial",
                "Riverhead": "Literary",
                "Morrow": "Commercial",
                "Penguin": "Commercial",
                "Vision": "Commercial",
                "Random" : "Commercial",
                "Knopf" : "Literary",
                "Simon & Schuster" : "Commercial",
                "Doubleday" : "Commercial",
                "St. Martin's" : "Commercial",
                "Jove" : "Genre",
                "Signet" : "Mystery/Crime",
                "Delacorte" : "Genre",
                "Pocket" : "Thriller/Horror",
                "Harlequin" : "Romance/Erotica",
                "Dutton": "Thriller/Horror",
                "Anchor" : "Literary",
                "Crown": "Commercial",
                "Mira" : "Commercial",
                "Back Bay" : "Commercial",
                "Ace" : "Science Fiction & Fantasy",
                "Washington Square": "Commercial",
                "Perennial": "Literary",
                "Viking": "Literary",
                "Atria" : "Genre",
                "Amy Einhorn" : "Literary",
                "HarperOne" : "Spiritual",
                "Vintage Crime/Black Lizard" : "Mystery/Crime",
                "Kensington" : "Commercial",
                "Tor" : "Science Fiction & Fantasy",
                "Emily Bestler" : "Commercial",
                "Gallery" : "Commercial",
                "Windblown Media" : "Spiritual",
                "Avon": "Romance/Erotica",
                "Picador": "Literary",
                "Frontline" : "Spiritual",
                "Algonquin" : "Literary",
                "St. Martin's Griffin" : "Commercial",
                "Del Rey" : "Science Fiction & Fantasy",
                "Plume" : "Literary",
                "Silhouette" : "Romance/Erotica",
                "Farrar, Straus & Giroux": "Literary",
                "Pamela Dorman" : "Commercial",
                "Vintage International": "Literary",
                "Europa" : "Literary",
                "Hyperion" : "Commercial",
                "Touchstone" : "Commercial",
                "Grove" : "Literary",
                "Roc" : "Science Fiction & Fantasy",
                "Pocket Star" : "Genre",
                "Ecco" : "Literary",
                "Scout" : "Literary",
                "Andrews McMeel" : "Humor & Games",
                "Marian Wood" : "Mystery/Crime",
                "HarperCollins" : "Commercial",
                "Three Rivers" : "Commercial",
                "Vintage Contemporaries" : "Literary",
                "Harper Paperbacks" : "Commercial",
                "Pantheon" : "Literary",
                "Entangled" : "Romance/Erotica",
                "Free" : "Literary",
                "Hard Case Crime" : "Mystery/Crime",
                "Forever" : "Romance/Erotica",
                "Forge" : "Genre",
                "Howard": "Spiritual",
                "Hogarth" : "Literary",
                "Deborah Bladon": "Romance/Erotica",
                "Sarah Crichton": "Literary",
                "Colleen Hoover" : "Romance/Erotica",
                "Mariner" : "Literary",
                "DAW" : "Science Fiction & Fantasy",
                "Flatiron" : "Commercial",
                "Waterhouse" : "Romance/Erotica",
                "Barbara Freethy" : "Romance/Erotica",
                "Berkley Sensation" : "Thriller/Horror",
                "Wizards of the Coast" : "Humor & Games",
                "New American Library" : "Commercial",
                "BookShots" : "Mystery/Crime",
                "Quirk" : "Humor & Games",
                "Helen Cooper" : "Romance/Erotica",
                "Threshold" : "Conservative",
                "Lauren Blakely" : "Romance/Erotica",
                "Delta" : "Commercial",
                "Orbit" : "Science Fiction & Fantasy",
                "Jessica Sorensen" : "Romance/Erotica",
                "Reagan Arthur" : "Literary",
                "Nan A. Talese" : "Literary",
                "Spiegel & Grau" : "Literary",
                "Tyndale" : "Spiritual",
                "J.C. Reed": "Romance/Erotica",
                "Laree Bailey" : "Romance/Erotica",
                "LucasBooks" : "Science Fiction & Fantasy",
                "Center Street" : "Conservative",
                "Bethany" : "Spiritual",
                "Abbi Glines" : "Romance/Erotica",
                "Thomas Nelson" : "Spiritual",
                "FaithWords" : "Spiritual",
                "Holt" : "Literary",
                "Witness Impulse" : "Mystery/Crime",
                "John Macrae" : "Literary",
                "Mullholland" : "Mystery/Crime",
                "Zondervan" : "Spiritual",
                "HTJB" : "Genre",
                "Jamie McGuire" : "Romance/Erotica",
                "InterMix" : "Genre",
                "Rachel Van Dyken" : "Romance/Erotica",
                "Houghton Mifflin Harcourt" : "Commercial",
                "Darcie Chan": "Romance/Erotica",
                "Zebra" : "Romance/Erotica",
                "Pinnacle" : "Thriller/Horror",
                "Vi Keeland" : "Romance/Erotica",
                "Tracey Garvis-Graves" : "Romance/Erotica",
                "Atlantic Monthly" : "Literary",
                "Kristen Ashley" : "Romance/Erotica",
                "Oak" : "Romance/Erotica",
                "Laurelin Paige" : "Romance/Erotica",
                "Gail McHugh" : "Romance/Erotica",
                "Kendall Ryan" : "Romance/Erotica",
                "Baen" : "Science Fiction & Fantasy",
                "Penelope Ward" : "Romance/Erotica",
                "Berkley Prime Crime" : "Mystery/Crime",
                "Samhain" : "Romance/Erotica",
                "Liveright" : "Literary",
                "Putnam Adult" : "Commercial",
                "Loveswept" : "Romance/Erotica",
                "Tijan" : "Romance/Erotica",
                "Sourcebooks" : "Genre",
                "Soho" : "Literary",
                "Jasinda Wilder" : "Romance/Erotica",
                "Thomas Dunne" : "Commercial",
                "Ellora's Cave" : "Romance/Erotica",
                "McSweeney's": "Literary",
                "Denise Grover Swank" : "Romance/Erotica",
                "Del Rey" : "Science Fiction & Fantasy",
                "Gossamer" : "Romance/Erotica",
                "Ampersand" : "Genre",
                "Harvest" : "Literary",
                "M. Leighton" : "Romance/Erotica",
                "EverAfter" : "Romance/Erotica",
                "Rutherford" : "Romance/Erotica",
                "Metal Blonde" : "Thriller/Horror",
                "Aurora Rose Reynolds" : "Romance/Erotica",
                "J.A. Redmerski" : "Romance/Erotica",
                "Catherine Bybee" : "Romance/Erotica",
                "H.M. Ward" : "Romance/Erotica",
                "Kingswell" : "Mystery/Crime",
                "Lisa Renee Jones" : "Romance/Erotica",
                "Addison Moore" : "Romance/Erotica",
                "Obsidian" : "Mystery/Crime",
                "DLZ Entertainment" : "Romance/Erotica",
                "Eos": "Science Fiction & Fantasy",
                "Brava" : "Romance/Erotica",
                "Avon Impulse" : "Romance/Erotica",
                "Grove/Atlantic" : "Literary",
                "Black Cat" : "Literary",
                "W. W. Norton": "Literary",
                "Morrow Impulse" : "Commercial",
                "Bloomsbury" : "Literary",
                "HQN" : "Romance/Erotica",
                "Voyager" : "Science Fiction & Fantasy",
                "Dial" : "Literary",
                "Bellevue Literary" : "Literary",
                "Minotaur" : "Science Fiction & Fantasy",
                "Michael Prescott" : "Mystery/Crime",
                "Chris Culver" : "Mystery/Crime",
                "Overlook" : "Literary",
                "Voice" : "Commercial",
                "Dorchester" : "Genre",
                "Stephanie McAfee" : "Commercial",
                "Penwyck" : "Commercial",
                "Legacy" : "Thriller/Horror",
                "Shaye Areheart" : "Commercial",
                "NAL Accent" : "Commercial",
                "El Leon Literary Arts" : "Literary",
                "CreateSpace" : "Genre",
                "Rerum" : "Romance/Erotica"
}
