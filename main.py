import re #module which works with regular expressions 
import os 

#Academic toolbox
#reference guide from UofA - https://www.adelaide.edu.au/library/ua/media/4063/library-qrg-harvard-referencing.pdf

#remove intext (good for academics)
#speech to text (openAI API) & text to speech (geeks - https://www.geeksforgeeks.org/convert-text-speech-python/)
#referencing using Adelaide Uni's standard (from input, you get the output)

#python main.py

def journal_articles(passed_num): 
    if passed_num == 1:
        first_name = input("Please enter author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p. x)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + '.' 
        return intext,reference
        
    elif passed_num == 2:
        date = input("Please enter the date that you accessed the journal in format of 'Date Month Year': ")
        url = input("Please enter the URL of the E-journal: ")
        first_name = input("Please enter author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p. x)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + 'viewed ' + date + ', ' + p_or_pp + ' ' + pages + ', ' + '<' + url + '>.' 
        return intext,reference
    
    elif passed_num == 3: 
        doi = input("Please enter the DOI: ")
        first_name = input("Please enter author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p. x)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + ', ' + 'DOI:' + doi + '.'
        return intext,reference
    
    elif passed_num == 4:
        doi = input("Please enter the DOI (Enter N/A if not present): ")
        date = input("Please enter the date that you accessed the journal in format of 'Date Month Year': ")
        url = input("Please enter the URL of the E-journal: ")
        first_name = input("Please enter author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p. x)'
        if (doi == 'N/A'):
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + ', ' + 'advance online publication' + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
        else:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + ', ' + 'advance online publication' + ', ' + 'DOI:' + doi + ', ' + '<' + url + '>.'
        return intext,reference
    
    elif passed_num == 5:
        first_name1 = input("Please enter the first author's first name: ")
        family_name1 = input("Please enter the first's author's family name: ")
        first_name2 = input("Please enter the second author's first name: ")
        family_name2 = input("Please enter the second author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name1 + ' & ' + family_name2 + ' ' + year + ', ' + 'p. x)'
        reference = family_name1 + ', ' + first_name1[0] + ' & ' + family_name2 + ', ' + first_name2[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + '.' 
        return intext,reference
        
    elif passed_num == 6:
        first_name1 = input("Please enter the first author's first name: ")
        family_name1 = input("Please enter the first's author's family name: ")
        first_name2 = input("Please enter the second author's first name: ")
        family_name2 = input("Please enter the second author's family name: ")
        first_name3 = input("Please enter the third author's first name: ")
        family_name3 = input("Please enter the third author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name1 + ', ' + family_name2 + ' & ' + family_name3 + ' ' + year + ', ' + 'p. x)'
        reference = family_name1 + ', ' + first_name1[0] + ', ' + family_name2 + ', ' + first_name2[0] + ' & ' + family_name3 + ', ' + first_name3[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + '.' 
        return intext,reference
    else: #num == 7
        first_name1 = input("Please enter the first author's first name: ")
        family_name1 = input("Please enter the first's author's family name: ")
        first_name2 = input("Please enter the second author's first name: ")
        family_name2 = input("Please enter the second author's family name: ")
        first_name3 = input("Please enter the third author's first name: ")
        family_name3 = input("Please enter the third author's family name: ")
        first_name4 = input("Please enter the fourth author's first name: ")
        family_name4 = input("Please enter the fourth author's family name: ")
        year = input("Please enter the initial year of publication: ")
        article_title = input("Please enter the title of the article: ")
        journal_title = input("Please enter the title of the journal: ")
        volume = input("Please enter the volume of the journal: ")
        issue = input("Please enter the issue number of the journal: ")
        pages = input("Please enter the page numbers that the journal article covers: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name1 + ' et al. ' + year + ', ' + 'p. x)'
        reference = family_name1 + ', ' + first_name1[0] + ', ' + family_name2 + ', ' + first_name2[0] + ', ' + family_name3 + ', ' + first_name3[0] + ' & ' + family_name4 + ', ' + first_name4[0] + ' ' + year + ', ' + "'"+article_title+"'" + ', ' + "\x1B[3m" + journal_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + '.' 
        return intext,reference
        

def books(passed_num):
    #8 to 18
    if passed_num == 8:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + '.'
        return intext,reference
        
    elif passed_num == 9:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the E-book: ")
        publisher = input("Please enter the name of the publisher of the E-book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that is being covered: ")
        doi = input("If a DOI is available, please enter it. If not, enter N/A: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p x.)'
        if (doi == 'N/A'):
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + '.'
        else:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + ', ' + 'DOI:' + doi + '.'
        return intext,reference
        
    elif passed_num == 10:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the E-book: ")
        publisher = input("Please enter the name of the publisher of the E-book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that is being covered: ")
        doi = input("If a DOI is available, please enter it. If not, enter N/A: ")
        date = input("Please enter the date that you accessed the journal in format of 'Date Month Year': ")
        url = input("Please enter the URL of the E-book: ")
        
        
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
            
        intext = '(' + family_name + ' ' + year + ', ' + 'p x.)'
        if (doi == 'N/A'):
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
        else:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + ', ' + 'DOI:' + doi + ', ' + '<' + url + '>.'
        return intext,reference
            
    elif passed_num == 11:
        first_name1 = input("Please enter the first author's first name: ")
        family_name1 = input("Please enter the first author's family name: ")
        first_name2 = input("Please enter the second author's first name: ")
        family_name2 = input("Please enter the second author's family name: ")
        first_name3 = input("Please enter the third author's first name. If there is no third author enter N/A: ")
        family_name3 = input("Please enter the third author's family name. If there is no third author enter N/A: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        if (first_name3 == 'N/A'):
             intext = '(' + family_name1 + ' & ' + family_name2 + ' '  + year + ', ' + 'p x.)'
             reference = family_name1 + ', ' + first_name1[0] + ', ' + family_name2 + ', ' + first_name2[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + '.'
        else:
            intext = '(' + family_name1 + ', ' + family_name2 + ' & ' + family_name3 + ' ' + year + ', ' + 'p x.)'
            reference = family_name1 + ', ' + first_name1[0] + ', ' + family_name2 + ', ' + first_name2[0] + ', ' + family_name3 + ', ' + first_name3[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + '.'
        
        return intext,reference
    
    elif passed_num == 12:
        first_name1 = input("Please enter the first author's first name: ")
        family_name1 = input("Please enter the first author's family name: ")
        first_name2 = input("Please enter the second author's first name: ")
        family_name2 = input("Please enter the second author's family name: ")
        first_name3 = input("Please enter the third author's first name: ")
        family_name3 = input("Please enter the third author's family name: ")
        first_name4 = input("Please enter the fourth author's first name: ")
        family_name4 = input("Please enter the fourth author's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
       
        intext = '(' + family_name1 + ' et al. ' + year + ', ' + 'p x.)'
        reference = family_name1 + ', ' + first_name1[0] + ', ' + family_name2 + ', ' + first_name2[0] + ', ' + family_name3 + ', ' + first_name3[0] + ', ' + family_name4 + ', ' + first_name4[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + '.'
        
        return intext,reference
        
    elif passed_num == 13:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        editor_first_name = input("Please enter the editor's first name: ")
        editor_family_name = input("Please enter the editor's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        chapter_title = input("Please enter the chapter's title: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
            
        intext = '(' + family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name1 + ', ' + first_name1[0] + ' ' + year + ', ' + "'" + chapter_title + "'" + ', ' + 'in ' + editor_first_name[0] + ' ' + editor_family_name + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + place_of_publication + ', ' + p_or_pp + ' ' + pages + '.'
        return intext,reference
        
    elif passed_num == 14:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        edition = input("Please enter the edition number of the book: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + edition + 'th' + ' edition, ' + publisher + ', ' + place_of_publication + '.'
        return intext,reference
    
    elif passed_num == 15:
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', ' + 'p x.)'
        reference = "\x1B[3m" + title + "\x1B[0m" + ' ' +  year + ', ' + publisher + ', ' + place_of_publication + '.'
        return intext,reference
    
    elif passed_num == 16:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        vol_num = input("Please enter the volume number: ")
        vol_title = input("Please enter the title of the volume: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + 'vol. ' + vol_num + ', ' + "\x1B[3m" + vol_title + "\x1B[0m" + ', '  + publisher + ', ' + place_of_publication + '.'
        return intext,reference
    
    elif passed_num == 17:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        translated_title = input("Please enter the translated title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ' (' + "\x1B[3m" + translated_title + "\x1B[0m" + ')' + ', ' + publisher + ', ' + place_of_publication + '.'
        return intext,reference
        
    else: #passed_num == 18
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        translator_first_name = input("Please enter the translator's first name: ")
        translator_family_name = input("Please enter the translator's family name: ")
        year = input("Please enter the publication year: ")
        title = input("Please enter the title of the book: ")
        publisher = input("Please enter the name of the publisher of the book: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + 'trans. ' + translator_first_name[0] + ' ' + translator_family_name  + ', '  + publisher + ', ' + place_of_publication + '.'
        return intext,reference

def conference_publications(passed_num):
    if passed_num == 19:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        editors_first_name = input("Please enter the editor's first name: ")
        editors_family_name = input("Please enter the editor's  family name: ")
        year = input("Please enter the publication year: ")
        paper_title = input("Please enter the title of the conference paper: ")
        conference_title = input("Please enter the title of the conference: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        conference_organiser = input("Please enter the organiser of the conference: ")
        
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + paper_title + "'" + ', in' +  editors_first_name[0] + ' ' + editors_family_name + ', ' + "\x1B[3m" + conference_title + "\x1B[0m" + ', ' + conference_organiser + ', ' + place_of_publication + ', ' + p_or_pp + ' ' + pages + '.'
        return intext,reference
        
    elif passed_num == 20:
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        editors_first_name = input("Please enter the editor's first name: ")
        editors_family_name = input("Please enter the editor's  family name: ")
        year = input("Please enter the publication year: ")
        paper_title = input("Please enter the title of the conference paper: ")
        conference_title = input("Please enter the title of the conference: ")
        place_of_publication = input("Please enter the place of publication (City): ")
        conference_organiser = input("Please enter the organiser of the conference: ")
        date = input("Please enter the date that you viewed the conference paper: ")
        url = input("Please enter the URL of the online conference paper: ")
        
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + paper_title + "'" + ', in' +  editors_first_name[0] + ' ' + editors_family_name + ', ' + "\x1B[3m" + conference_title + "\x1B[0m" + ', ' + conference_organiser + ', ' + place_of_publication + ', ' + p_or_pp + ' ' + pages + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
        return intext,reference
        
    else: #passed_num == 21
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year: ")
        paper_title = input("Please enter the title of the conference paper: ")
        conference_title = input("Please enter the title of the conference: ")
        conference_location = input("Please enter the location of the conference: ")
        date = input("Please enter the date that the conference occured (in dd-dd month format): ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + paper_title + "'" + ', paper presented at ' + "\x1B[3m" + conference_title + "\x1B[0m" + ', ' + conference_location + ', ' + date + '.'
        return intext,reference

def newspaper_or_magazine(passed_num):
    if passed_num == 22:
        
        choice = int(input("Does your magazine/newspaper have a date of publication (dob) or volume and issue (v&i). Enter 1 for dob and 2 for v&i: "))
        os.system('cls')
        if (choice == 1):
            date = input("Please enter the date that the conference occured (in dd month format): ")
        else:
            volume = input("Please enter the volume for the newspaper/magazine: ")
            issue = input("Please enter the issue for the newspaper/magazine")
            
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year of the newspaper/magazine: ")
        article_title = input("Please enter the title of the newspaper/magazine: ")
        newspaper_or_magazine_title = input("Please enter the title of the newspaper/magazine: ")
        pages = input("Please enter the page numbers that are being covered: ")
        
        cur_page = int(pages)
        p_or_pp = 'null'
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = ''
        if choice == 1:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + article_title + "'" + "\x1B[3m" + newspaper_or_magazine_title + "\x1B[0m" + ', ' + date + ', ' + p_or_pp + ' ' + pages + '.'
        else:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + article_title + "'" + "\x1B[3m" + newspaper_or_magazine_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + '.'
            
        return intext, reference
            
    elif passed_num == 23:
        choice = int(input("Does your magazine/newspaper have a date of publication (dob) or volume and issue (v&i). Enter 1 for dob and 2 for v&i: "))
        os.system('cls')
        if (choice == 1):
            date = input("Please enter the date that the conference occured (in dd month format): ")
        else:
            volume = input("Please enter the volume for the newspaper/magazine: ")
            issue = input("Please enter the issue for the newspaper/magazine")
            
        first_name = input("Please enter the author's first name: ")
        family_name = input("Please enter the author's family name: ")
        year = input("Please enter the publication year of the online newspaper/magazine: ")
        article_title = input("Please enter the title of the online newspaper/magazine: ")
        newspaper_or_magazine_title = input("Please enter the title of the online newspaper/magazine: ")
        pages = input("Please enter the page numbers that are being covered: ")
        date = input("Please enter the date that you viewed the online newspaper/magazine: ")
        url = input("Please enter the URL of the online magazine/newspaper: ")
        
        cur_page = int(pages)
        p_or_pp = 'null'
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  family_name + ' ' + year + ', ' + 'p x.)'
        reference = ''
        if choice == 1:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + article_title + "'" + "\x1B[3m" + newspaper_or_magazine_title + "\x1B[0m" + ', ' + date + ', ' + p_or_pp + ' ' + pages + ', viewed' + date + ', ' + '<' + url + '>.'
        else:
            reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "'" + article_title + "'" + "\x1B[3m" + newspaper_or_magazine_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + ', viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference
        
    else: #passed_num == 24
        choice = int(input("Does your magazine/newspaper have a date of publication (dob) or volume and issue (v&i). Enter 1 for dob and 2 for v&i: "))
        os.system('cls')
        if (choice == 1):
            date = input("Please enter the date that the conference occured (in dd month format): ")
        else:
            volume = input("Please enter the volume for the newspaper/magazine: ")
            issue = input("Please enter the issue for the newspaper/magazine")
            
        publication_name = input("Please enter the name of the publisher of the newspaper/magazine: ") 
        year = input("Please enter the publication year of the newspaper/magazine: ")
        article_title = input("Please enter the title of the newspaper/magazine: ")
        newspaper_or_magazine_title = input("Please enter the title of the newspaper/magazine: ")
        pages = input("Please enter the page numbers that are being covered: ")
        date = input("Please enter the date that you viewed the newspaper/magazine: ")
        url = input("Please enter the URL of the magazine/newspaper: ")
        
        cur_page = int(pages)
        p_or_pp = 'null'
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' +  publication_name + ' ' + year + ', ' + 'p x.)'
        reference = ''
        if choice == 1:
            reference = publication_name + ' ' + year + ', ' + "'" + article_title + "'" + "\x1B[3m" + newspaper_or_magazine_title + "\x1B[0m" + ', ' + date + ', ' + p_or_pp + ' ' + pages + ', viewed' + date + ', ' + '<' + url + '>.'
        else:
            reference = publication_name + ' ' + year + ', ' + "'" + article_title + "'" + "\x1B[3m" + newspaper_or_magazine_title + "\x1B[0m" + ', ' + 'vol. ' + volume + ', ' + 'no. ' + issue + ', ' + p_or_pp + ' ' + pages + ', viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference

def reference_work(passed_num):
    if passed_num == 25:
        author = input("Please enter the author of the book: ")
        title = input("Please enter the title of the book: ")
        year = input("Please enter the year of publication of the book: ")
        
        
        cur_page = int(pages)
        p_or_pp = 'null'
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
            
        
        return intext,reference
        
    elif passed_num == 26:
        pass
    elif passed_num == 27:
        pass
    else: #passed_num == 28 
        

def dataset(passed_num):
    pass

def webpage(passed_num):
    pass

def social_media(passed_num):
    pass

def audio_visual(passed_num):
    pass

def image(passed_num):
    pass

def reference_types(passed_num):
    pass 



#function which looks for a year in the bracketed string. If a year is found, 
#then this means that the bracketed string is an intext reference 
def find_year(cur_intext):
    year = r'\b\d{4}\b' #creating a raw string literal (https://www.w3schools.com/python/python_regex.asp) (the r denotes that \b is a special character not just literal \b)
    match = re.search('year', cur_intext)
    return bool(match)
    
    
    
#function which removes the intext referencing from the given text 
#if there is a year in the intext, then the brackets will be removed 
def get_intext(cur_text):
    bracket_one = False
    bracket_one_index = 0
    bracket_two = False 
    bracket_two_index = 0 
    for index, letter in enumerate(cur_text):
        if (letter == '('):
            bracket_one = True
            bracket_one_index = index
        if (letter == ')'):
            bracket_two = True 
            bracket_two_index = index 
        if (bracket_one == True and bracket_two == True):
            bracket_one = False
            bracket_two = False
            current_intext = cur_text[bracket_one_index-1:bracket_two_index+1] 
            result = find_year(current_intext)
            if result == True: 
                cur_text = cur_text.replace(current_intext, '')
                
    return cur_text
                
            
#function which gets the word count of text                                
def word_count(cur_text):  
    words = 0 
    word_length = len(cur_text) 
    for index, letter in enumerate(cur_text):
        if letter == " ":   
            words = words  + 1
        if index == word_length-1:
            words = words + 1    
    return words
    
        

def main():
        
        choice = '0'
        while choice != '1' and choice != '2':
            choice = input("Enter 1 for removing intext referencing, 2 for getting the intext and reference list version of the source (Harvard referencing style for The University of Adelaide).\n")
        
        os.system('cls')
        
        if choice == '1':
            #to copy and paste in terminal simply do right click on the mouse
            main_text = main_text.rstrip() #tstrip() removes leading and trailing whitespace
            old_wordcount = word_count(main_text)
            main_text = get_intext(main_text)
            new_wordcount = word_count(main_text)
            print("The old word count is: ", old_wordcount)
            print("The new word count is: ", new_wordcount)
            print("Your modified text: ", main_text)
        else:
            #journal articles
            print("Journal articles: ")
            print("1. Journal article from UofA database")
            print("2. Journal article from the Web")
            print("3. Journal article with DOI")
            print("4. Journal article in press/advance online publication")
            print("5. Journal article with 2 authors")
            print("6. Journal article with 3 authors")
            print("7. Journal article with 4 or more authors\n")
            
            #books 
            print("Books: ")
            print("8. Book in print")
            print("9. Book that is an E-book (from UofA database)")
            print("10. Book that is an E-book (from web)")
            print("11. Book that has two or three authors")
            print("12. Book that has four or more authors")
            print("13. Book chapter in an edited book")
            print("14. Book with an edition number")
            print("15. Book with no author")
            print("16. Book with a volume number")
            print("17. Book written in foreign language")
            print("18. Book translated from a foreign language\n")
            
            #conference publications 
            print("Conference papers: ")
            print("19. Conference paper published in edited book of proceedings (in print or accessed from UofA database)")
            print("20. Conference paper published online")
            print("21. Conference presentation (unpublished)\n")
            
            #Newspaper or magazine article 
            print("Newspaper or magazine articles: ")
            print("22. In print")
            print("23. Online")
            print("24. No author\n")
            
            #Reference work 
            print("Reference work: ")
            print("25. Dictionary")
            print("26. Classics")
            print("27. Encyclopedia entry")
            print("28. Encyclopedia entry without an author\n")
            
            #Dataset
            print("Dataset: ")
            print("29. With DOI")
            print("30. Without DOI\n")
            
            #Webpage
            print("Webpage: ")
            print("31. Website")

            #Social media 
            print("Social media: ")
            print("32. Blog")
            print("33. Blog post")
            print("34. Facebook post")
            print("36. Tweet\n")

            #Audiovisual 
            print("Audiovisual: ")
            print("37. Youtube")
            print("38. Television broadcast")
            print("39. Video / Film / DVD")
            print("40. Podcast")
            print("41. Radio programme\n")
            
            #Image 
            print("Image: ")
            print("42. Artwork")
            print("43. Picture/Graph\n")
            
            #Other reference types
            print("Other reference types: ")
            print("44. Australian Bureau of Statistics")
            print("45. Emails, phone conversation, letters, interviews")
            print("46. Lecture notes given out during a lecture")
            print("47. Your own notes taken during a lecture")
            print("48. Map")
            print("49. Patent")
            print("50. Powerpoint presentation")
            print("51. Report")
            print("52. Reports by organisations without a specific author")
            print("53. Thesis\n")
            
            reference_item = int(input("What type of reference do you need? Enter the number that is next to the name: \n")) 
            
            os.system('cls')
            
            if 1 <= reference_item <= 7:
                intext, reference = journal_articles(reference_item)
            elif 8 <= reference_item <= 18:
                intext, reference = books(reference_item)
            elif 19 <= reference_item <= 21:
                intext, reference = conference_publications(reference_item)
            elif 22 <= reference_item <= 24:
                intext, reference = newspaper_or_magazine(reference_item)
            elif 25 <= reference_item <= 28:
                intext, reference = reference_work(reference_item)
            elif 29 <= reference_item <= 30:
                intext, reference = dataset(reference_item)
            elif reference_item == 31:
                intext, reference = webpage(reference_item)
            elif 32 <= reference_item <= 36:
                intext, reference = social_media(reference_item)
            elif 37 <= reference_item <= 41:
                intext, reference = audio_visual(reference_item)
            elif 42 <= reference_item <= 43:
                intext, reference = image(reference_item)
            else: #other reference types
                intext, reference = reference_types(reference_item)    
                
                
            os.system('cls')    
            print("The intext reference (where x is the page number): ", intext)
            print("The reference itself: ", reference)
            
            
main() #calls main function  
    