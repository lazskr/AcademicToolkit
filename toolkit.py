import re #module which works with regular expressions 
import os #user can interact with the operating systen 
from gtts import gTTS #gTTS tool from gtts library used for text to speech
import requests #used to send a post request to openAI's API and to recieve a response back 

#function which creates a reference and intext reference for the user for the type of journal article reference that they selected 
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
        


#function which creates a reference and intext reference for the user for the type of book reference that they selected 
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
        
        if int(edition) == 1:
            type = 'st'
        elif int(edition) == 2:
            type = 'nd'
        elif int(edition) == 3:
            type = 'rd'
        else:
            type = 'th'
        
        cur_page = int(pages)
        if cur_page > 10:
            p_or_pp = 'pp.'
        else:
            p_or_pp = 'p.'
        
        intext = '(' + family_name + ' ' + year + ', ' + 'p x.)'
        reference = family_name + ', ' + first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + edition + type + ' edition, ' + publisher + ', ' + place_of_publication + '.'
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



#function which creates a reference and intext reference for the user for the type of conference publication reference that they selected 
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



#function which creates a reference and intext reference for the user for the type of newspaper/magazine reference that they selected 
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



#function which creates a reference and intext reference for the user for the type of reference work that they selected 
def reference_work(passed_num):
    if passed_num == 25:
        title = input("Please enter the title of the dictionary: ")
        year = input("Please enter the year that the dictionary was published: ")
        edition = input("Please enter the edition of the dictionary: ")
        volume = input("Please input the volume of the dictionary: ")
        publisher = input("Please enter the publisher of the dictionary: ")
        publisher_location = input("Please enter the location of the publisher: ")
        
        if int(edition) == 1:
            type = 'st'
        elif int(edition) == 2:
            type = 'nd'
        elif int(edition) == 3:
            type = 'rd'
        else:
            type = 'th'
            
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', p. x)'
        reference =  "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', ' + edition + type + ' edn, ' + 'vol. ' + volume + ', ' + publisher + ', ' + publisher_location + '.'
       
        return intext,reference
        
    elif passed_num == 26:
        author_family_name = input("Please enter the family name of the author: ")
        title = input("Please enter the title of the book: ")
        translor_first_name = input("Please enter the translator's first name: ")
        translator_family_name = input("Please enter the translator's family name: ")
        publisher = input("Please enter the name of the publisher: ")
        publication_location = input("Please enter the location of the publisher: ")
        publication_year = input("Please enter the year of publication: ")
        book_number = input("Please enter the book number: ")
        line_numbers = input("Please enter the line numbers that are being covered: ")
        
        intext = '(' + author_family_name + ' ' + title + ', ' + book_number + '.' + line_numbers + ')'
        reference = author_family_name + '.' + ' ' + "\x1B[3m" + title + "\x1B[0m" + ', translated by ' + translor_first_name[0] + '.' + ' ' + translator_family_name + '. ' + publication_location + '. ' + publisher + '. ' + publication_year + '.'
            
        return intext,reference
    
    elif passed_num == 27:
        authors_first_name = input("Please enter the first name of the author: ")
        authors_family_name = input("Please enter the family name of the author: ")
        title = input("Please enter the title of the encyclopedia: ")
        year = input("Please enter the year that the encyclopedia was published: ")
        edition = input("Please enter the edition of the encyclopedia: ")
        publisher = input("Please enter the publisher of the encyclopedia: ")
        publisher_location = input("Please enter the location of the publisher: ")
        
        if int(edition) == 1:
            type = 'st'
        elif int(edition) == 2:
            type = 'nd'
        elif int(edition) == 3:
            type = 'rd'
        else:
            type = 'th'
            
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', p. x)'
        reference =  authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + edition + type + ' edn, ' + ', ' + publisher + ', ' + publisher_location + '.'
       
        return intext,reference
    
    else: #passed_num == 28 
        title = input("Please enter the title of the encyclopedia: ")
        year = input("Please enter the year that the encyclopedia was published: ")
        edition = input("Please enter the edition of the encyclopedia: ")
        volume = input("Please input the volume of the encyclopedia: ")
        publisher = input("Please enter the publisher of the encyclopedia: ")
        publisher_location = input("Please enter the location of the publisher: ")
        
        if int(edition) == 1:
            type = 'st'
        elif int(edition) == 2:
            type = 'nd'
        elif int(edition) == 3:
            type = 'rd'
        else:
            type = 'th'
            
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', p. x)'
        reference =  "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', ' + edition + type + ' edn, ' + 'vol. ' + volume + ', ' + publisher + ', ' + publisher_location + '.'
       
        return intext,reference
        


#function which creates a reference and intext reference for the user for the type of dataset reference that they selected     
def dataset(passed_num):
    if passed_num == 29:
        choice = input("Is there an author present on the dataset? Enter 1 for yes and 2 for no: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author: ")
            authors_family_name = input("Please enter the family name of the author: ")
        else: 
            authoring_body = input("Please enter the name of the authoring body (e.g., company or department): ")
            
        year = input("Please enter the year that the dataset was published: ")
        title = input("Please enter the title of the dataset: ")
        doi = input("Please enter the DOI of the datset: ")
        
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + 'DOI: ' + doi + '.'
        else: 
            intext = '(' + authoring_body + ' ' + year + ')'
            reference = authoring_body + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + 'DOI: ' + doi + '.'
    
        return intext, reference 
                
    else: #passed_num == 30
        choice = input("Is there an author present on the dataset? Enter 1 for yes and 2 for no: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author: ")
            authors_family_name = input("Please enter the family name of the author: ")
        else: 
            authoring_body = input("Please enter the name of the authoring body (e.g., company or department): ")
            
        year = input("Please enter the year that the dataset was published: ")
        title = input("Please enter the title of the dataset: ")
        date = input("Please enter the date you viewed the dataset (dd mm year format): ")
        url = input("Please enter the URL of the dataset: ")
        
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
        else: 
            intext = '(' + authoring_body + ' ' + year + ')'
            reference = authoring_body + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
    
        return intext, reference 
        
        
        
#function which creates a reference and intext reference for a website          
def webpage(passed_num): #passed_num == 31
    choice = input("Is there an author present on the webpage? Enter 1 for yes and 2 for no: ")
    if choice == 1:
        authors_first_name = input("Please enter the first name of the author: ")
        authors_family_name = input("Please enter the family name of the author: ")
    else: 
        authoring_body = input("Please enter the name of the authoring body (e.g., company or department): ")
        
    year = input("Please input the year that the webpage was published or last updated (if there is no year use 'n.d.'): ")
    title = input("Please enter the title of the webpage: ")
    website_title = input("Please enter the title of the webpage: ")
    date = input("Please enter the date you viewed the webpage (dd mm year format): ")
    url = input("Please enter the URL of the webpage: ")
    
    if choice == 1:
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + website_title + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
    else: 
        intext = '(' + authoring_body + ' ' + year + ')'
        reference = authoring_body + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + website_title + ', ' + 'viewed ' + date + ', ' + '<' + url + '>.'
        
    return intext, reference 



#function which creates a reference and intext reference for the user for the type of social media reference that they selected 
def social_media(passed_num):
    if passed_num == 32:
        choice = input("Enter 1 to enter the author's first and family name. Enter 2 to enter the author's username: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author of the blog: ")
            authors_family_name = input("Please enter the family name of the author: ")
        else: 
            username = input("Please enter the username of the user who runs the blog of the blog: ")
            
        blog_name = input("Please enter the blog's name: ")
        year = input("What year was the blog post published: ")
        date = input("Please enter the date you viewed the webpage (dd mm year format): ")
        url = input("Please enter the URL of the webpage: ")
            
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + blog_name + "\x1B[0m" + ', blog, viewed' + date + ', ' + '<' + url + '>.'
        else:
            intext = '(' + username + ' ' + year + ')'
            reference = username + ' ' + year + ', ' + "\x1B[3m" + blog_name + "\x1B[0m" + ', blog, viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference    

    elif passed_num == 33:
        choice = input("Enter 1 to enter the author's first and family name. Enter 2 to enter the author's username: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author of the blog post: ")
            authors_family_name = input("Please enter the family name of the author of the blog post: ")
        else: 
            username = input("Please enter the username of the user who runs the blog: ")
            
        blog_name = input("Please enter the blog's name: ")
        blog_post = input("Please enter the name of the blog post: ")
        year = input("What year was the blog post published: ")
        date = input("Please enter the date you viewed the webpage (dd mm year format): ")
        url = input("Please enter the URL of the webpage: ")
            
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "'" + blog_post + "'" + ', ' + "\x1B[3m" + blog_name + "\x1B[0m" + ', blog post, viewed' + date + ', ' + '<' + url + '>.'
        else:
            intext = '(' + username + ' ' + year + ')'
            reference = username + ' ' + year + ', ' + "'" + blog_post + "'" + ', ' + "\x1B[3m" + blog_name + "\x1B[0m" + ', blog post, viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference 
        
    elif passed_num == 34:
        choice = input("Enter 1 to enter the author's first and family name. Enter 2 to enter the author's username: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author of the Facebook post: ")
            authors_family_name = input("Please enter the family name of the author of the Facebook post: ")
        else: 
            username = input("Please enter the username of the Facebook user: ")
            
        facebook_post = input("Please enter the name of the Facebook post: ")
        year = input("What year was the Facebook post published: ")
        date = input("Please enter the date you viewed the Facebook post (dd mm year format): ")
        url = input("Please enter the URL of the Facebook post: ")
            
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + "\x1B[3m" + facebook_post + "\x1B[0m" + ', Facebook, viewed' + date + ', ' + '<' + url + '>.'
        else:
            intext = '(' + username + ' ' + year + ')'
            reference = username + ' ' + year + ', ' + "\x1B[3m" + facebook_post + "\x1B[0m" + ', Facebook, viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference 
        
    else: #passed_num == 35 
        choice = input("Enter 1 to enter the author's first and family name. Enter 2 to enter the author's username: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author of the tweet: ")
            authors_family_name = input("Please enter the family name of the author of the tweet: ")
        else: 
            username = input("Please enter the username of the Twitter user: ")
            
        tweet = input("Please enter the name of the tweet: ")
        year = input("What year was the Twitter post published: ")
        date = input("Please enter the date you viewed the Twitter post (dd mm year format): ")
        url = input("Please enter the URL of the Twitter post: ")
            
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + "\x1B[3m" + tweet + "\x1B[0m" + ', Twitter, viewed' + date + ', ' + '<' + url + '>.'
        else:
            intext = '(' + username + ' ' + year + ')'
            reference = username + ' ' + year + ', ' + "\x1B[3m" + tweet + "\x1B[0m" + ', Twitter, viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference 



#function which creates a reference and intext reference for the user for the type of audio visual reference that they selected 
def audio_visual(passed_num):
    if passed_num == 36:
        choice = input("Enter 1 to enter the author's first and family name. Enter 2 to enter the author's username: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author of the YouTube video: ")
            authors_family_name = input("Please enter the family name of the author of the YouTube video: ")
        else: 
            username = input("Please enter the username of the YouTube user: ")
            
        youtube_video = input("Please enter the name of the YouTube video: ")
        year = input("What year was the YouTube video published: ")
        date = input("Please enter the date you viewed the YouTube video (dd mm year format): ")
        url = input("Please enter the URL of the YouTube video: ")
            
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + "\x1B[3m" + youtube_video + "\x1B[0m" + ', YouTube, viewed' + date + ', ' + '<' + url + '>.'
        else:
            intext = '(' + username + ' ' + year + ')'
            reference = username + ' ' + year + ', ' + "\x1B[3m" + youtube_video + "\x1B[0m" + ', YouTube, viewed' + date + ', ' + '<' + url + '>.'
            
        return intext, reference 
        
    elif passed_num == 37:
        title = input("Please enter the title of the television show: ")
        year = input("What year was the television show filmed: ")
        broadcaster = input("What is the name of the broadcaster: ")
        place = input("Where was the television show filmed: ")
        date = input("What date was the television show filmed (dd mm format): ")
        
        intext = '(' + title + ' ' + year + ')'
        reference = "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', television programme, ' + broadcaster + ', ' + place + ', ' + date + '.'
        
        return intext, reference 
        
    elif passed_num == 38:
        title = input("Please enter the title of the television show: ")
        episode = input("Please enter the title of the episode: ")
        year = input("What year was the television show filmed: ")
        broadcaster = input("What is the name of the broadcaster: ")
        place = input("Where was the television show filmed: ")
        
        intext = '(' + title + ' ' + year + ')'
        reference = "\x1B[3m" + episode + "\x1B[0m" + ' ' + year + ', television series episode, in ' + title + ', ' + broadcaster + ', ' + place + '.'
        
        return intext, reference 
    
    elif passed_num == 39:
        choice = input("If this is for a video enter 1, enter 2 for film and enter 3 for dvd: ")
        if choice == 1:
            choice = 'video'
        elif choice == 2: 
            choice = 'film'
        else: 
            choice = 'dvd'
            
        title = input("Please input the title for the " + choice + ':')
        year = input("Please enter the year that the " + choice + ' was published: ')
        producer = input("Please enter the producer of the " + choice + ':')
        publisher_location = input("Please enter the year that the " + choice + ' was published: ')
        
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ')'
        reference = "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', ' + choice + ', ' + producer + ', ' + publisher_location + '.'
        
        return intext,reference
        
    elif passed_num == 40: 
        choice = input("Enter 1 to enter the author's first and family name. Enter 2 to enter the podcast's name: ")
        if choice == 1:
            authors_first_name = input("Please enter the first name of the author of the YouTube video: ")
            authors_family_name = input("Please enter the family name of the author of the YouTube video: ")
        else: 
            podcast_name = input("Please enter the podcast's name: ")
            
        podcast_episode = input("Please enter the podcast's episode name: ")
        year = input("What year was the podcast episode published: ")
        date = input("Please enter the date the podcast was published (dd mm year format): ")
        date_viewed = input("Please enter the date that you viewed the podcast")
        url = input("Please enter the URL of the podcast: ")
            
        if choice == 1:
            intext = '(' + authors_family_name + ' ' + year + ')'
            reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + podcast_episode + "\x1B[0m" + ', podcast, ' + date + ', viewed ' + date_viewed + ', ' '<' + url + '>.'
        else:
            intext = '(' + podcast_name + ' ' + year + ')'
            reference = podcast_name + ' ' + year + ', ' + "\x1B[3m" + podcast_episode + "\x1B[0m" + ', podcast, ' + date + ', viewed ' + date_viewed + ', ' '<' + url + '>.'
            
        return intext, reference 
    
    else: #passed_num == 41
        title = input("Please enter the title of the radio programme: ")
        year = input("Please enter the year that the radio programme was published: ")
        broadcaster = input("Please enter the name of the broadcaster of the radio programme: ")
        place = input("Please enter the location that the radio programme occured: ")
        date = input("Please enter the date that the radio programme was recorded (dd mm format): ")
        
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ')'
        reference = "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', radio programme, ' + broadcaster + ', ' + place + ', ' + date + '.'



#function which creates a reference and intext reference for the user for the type of image reference that they selected 
def image(passed_num):
    if passed_num == 42:
        artists_first_name = input("Please enter the first name of the artist ")
        artists_family_name = input("Please enter the family name of the artist: ")
        year = input("Please enter the year that the artwork was made: ")
        title = input("Please enter the title of the artwork: ")
        item_type = input("Please enter the type of the item: ")
        place = input("Please enter the location that the artwork is kept: ")
        date = input("Please enter the date that the artwork was viewed (in dd mm year format): ")
        
        intext = '(' + artists_family_name + ' ' + year + ')'
        reference = artists_family_name + ', ' + artists_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + item_type + ', ' + place + ', viewed ' + date + '.'
        
        return intext,reference
        
    elif passed_num == 43:
        artists_first_name = input("Please enter the first name of the artist ")
        artists_family_name = input("Please enter the family name of the artist: ")
        year = input("Please enter the year that the artwork was made: ")
        title = input("Please enter the title of the artwork: ")
        medium = input("Please enter the medium that you viewed the artwork on: ")
        website = input("Please enter the name of the website: ")
        place = input("Please enter the location that the artwork is kept: ")
        date = input("Please enter the date that the artwork was viewed (in dd mm year format): ")
        url = input("Please enter the URL that was viewed which contains the artwork: ")
        
        intext = '(' + artists_family_name + ' ' + year + ')'
        reference = artists_family_name + ', ' + artists_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + medium + ', ' + website + ', ' + place + ', viewed ' + date + ', ' + '<' + url + '>.'
        
        return intext,reference
    
    else: #passed_num == 44
        authors_first_name = input("Please enter the first name of the author ")
        authors_family_name = input("Please enter the family name of the author: ")
        year = input("Please enter the year that the picture/graph was made: ")
        title = input("Please enter the title of the picture/graph: ")
        date = input("Please enter the date that the picture/graph was viewed (in dd mm year format): ")
        url = input("Please enter the URL that was viewed which contains the picture/graph: ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', viewed ' + date + ', ' + '<' + url + '>.'
        
        return intext,reference



#function which creates a reference and intext reference for the user for a specific reference type that they selected
def reference_types(passed_num):
    if passed_num == 45:
        title = input("Please enter the title of the Australian Bureau of Statistics (ABS) page: ")
        year = input("Please enter the year that the ABS page was published: ")
        catalog_number: input("Please enter the catalog number: ")
        date = input("Please enter the date that you have viewed the ABS page: ")
        url = input("Please enter the URL of the ABS page: ")
        
        intext = '(Australian Bureau of Statistics ' + year + ')'
        reference = 'Australian Bureau of Statistics ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', cat. no. ' + catalog_number + ', ABS, viewed ' + date + '<' + url + '>.'
        
        return intext, reference
        
    elif passed_num == 46:
        
        choice = input("What type of personal communication is being referenced? Enter 1 for email, 2 for phone conversation, 3 for letter and 4 for interview: ")
        if choice == 1:
            choice = 'email'
        elif choice == 2:
            choice = 'phone conversation'
        elif choice == 3:
            choice = 'letter'
        else: 
            choice = 'interview'
        authors_family_name = input("Please enter the family name of the individual on the other end of the" + choice + ': ')
        date = input("Please enter the date that the " + choice + ' took place: ')
        
        intext = '(' + authors_family_name + ', ' + choice + ', ' + date + ')'
        reference = "There is no reference required."
        
        return intext, reference 
        
    elif passed_num == 47:
        authors_first_name = input("Please enter the first name of the lecturer: ")
        authors_family_name = input("Please enter the family name of the lecturer: ")
        year = input("Please enter the year that the lecture was made: ")
        title = input("Please enter the title of the lecture: ")
        lecture_topic = input("Please enter the name of the lecture topic: ")
        institution = input("Please enter the name of the institution (university or otherwise) which published the lecture: ")
        date = input("Please enter the date that the lecture was published (in dd mm year format): ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "'" + title + "'" + ', lecture notes distributed in the topic ' + lecture_topic + ', ' + institution + ', on ' + date + '.' 
        
        
    elif passed_num == 48:
        intext = "The intext should follow this formatting: 'During a lecture in the topic 7052 'Electromagnetic theory and RFID applications' given at the University of Adelaide on 12 July 2010, Professor Peter Cole said ...'"
        reference = "No reference required."
        return intext, reference 
    
    elif passed_num == 49:
        authors_first_name = input("Please enter the first name of the map maker: ")
        authors_family_name = input("Please enter the family name of the map maker: ")
        year = input("Please enter the year that the map was made: ")
        title = input("Please enter the title of the map: ")
        scale = input("Please enter the scale of the map: ")
        publisher = input("Please enter the publisher of the map: ")
        publisher_location = input("Please enter the publisher's location: ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + scale + ', ' + publisher + ', ' + publisher_location + '.'
        
        return intext, reference 
        
    elif passed_num == 50:
        authors_first_name = input("Please enter the first name of the patent maker: ")
        authors_family_name = input("Please enter the family name of the patent maker: ")
        year = input("Please enter the year that the pantent was made: ")
        title = input("Please enter the title of the patent: ")
        patent_details = input("Please enter the patent details (e.g., 'Australian Patent 215772'): ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + patent_details + '.'
        
        return intext, reference       
        
    elif passed_num == 51:
        authors_first_name = input("Please enter the first name of the Powerpoint: ")
        authors_family_name = input("Please enter the family name of the Powerpoint: ")
        year = input("Please enter the year that the Powerpoint was made: ")
        title = input("Please enter the title of the Powerpoint: ")
        date = input("Please enter the date that you viewed the Powerpoint: ")
        url = input("Please enter the URL of the Powerpoint: ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "'" + title + "'" + ', PowerPoint presentation, viewed ' + date + '<' + url + '>.'
        
        return intext, reference 
        
    elif passed_num == 52:
        authors_first_name = input("Please enter the first name of the report: ")
        authors_family_name = input("Please enter the family name of the report: ")
        year = input("Please enter the year that the report was made: ")
        title = input("Please enter the title of the report: ")
        publisher = input("Please enter the publisher of the report: ")
        publisher_location = input("Please enter the publisher's location: ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "\x1B[3m" + title + "\x1B[0m" + ', ' + publisher + ', ' + publisher_location + '.'
        
        return intext, reference 
        
    elif passed_num == 53:
        year = input("Please enter the year that the report was made: ")
        title = input("Please enter the title of the report: ")
        organisation = input("Please enter the name of the organisation which published the report: ")
        publisher = input("Please enter the publisher of the report: ")
        publisher_location = input("Please enter the publisher's location: ")
        date = input("Please enter the date that you viewed the report: ")
        url = input("Please enter the URL of the report: ")
        
        intext = '(' + "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ')'
        reference = "\x1B[3m" + title + "\x1B[0m" + ' ' + year + ', ' + organisation + ', ' + publisher + ', ' + publisher_location + ', viewed ' + date + ', ' + '<' + url + '>.'
        
        return intext, reference 
        
    else: #passed_num == 54
        authors_first_name = input("Please enter the first name of the report: ")
        authors_family_name = input("Please enter the family name of the report: ")
        year = input("Please enter the year that the report was made: ")
        title = input("Please enter the title of the report: ")
        thesis_type = input("Please enter the type of thesis (e.g., 'MA thesis'): ")
        institution = input("Please enter the name of the institution (university or otherwise) which the thesis is associated with: ")
        institution_location = input("Where is the institution located in (city): ")
        
        intext = '(' + authors_family_name + ' ' + year + ')'
        reference = authors_family_name + ', ' + authors_first_name[0] + ' ' + year + ', ' + "'" + title + "'" + ', ' + thesis_type + ', ' + institution + ', ' + institution_location + '.'

        return intext, reference 



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
        
        #There are 4 main features in this program. The user decides which one they would like 
        choice = '0'
        while choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = input("Enter 1 for removing intext referencing, 2 for getting the intext and reference list version of the source (Harvard referencing style for The University of Adelaide), 3 for generating text to speech or 4 for generating speech to text. \n")
        
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
        elif choice == '2':
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
            print("35. Tweet\n")

            #Audiovisual 
            print("Audiovisual: ")
            print("36. Youtube")
            print("37. Television broadcast")
            print("38. Video / Film / DVD")
            print("39. Video / Film / DVD for specific episode")
            print("40. Podcast")
            print("41. Radio programme\n")
            
            #Image 
            print("Image: ")
            print("42. Artwork")
            print("43. Artwork viewed online")
            print("44. Picture/Graph\n")
            
            #Other reference types
            print("Other reference types: ")
            print("45. Australian Bureau of Statistics")
            print("46. Emails, phone conversation, letters, interviews")
            print("47. Lecture notes given out during a lecture")
            print("48. Your own notes taken during a lecture")
            print("49. Map")
            print("50. Patent")
            print("51. Powerpoint presentation")
            print("52. Report")
            print("53. Reports by organisations without a specific author")
            print("54. Thesis\n")
            
            reference_item = int(input("What type of reference do you need? Enter the number that is next to the name: \n")) 
            
            os.system('cls')
            
            #determining what type of reference that the user has chosen and calling 
            #the associated function 
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
            elif 32 <= reference_item <= 35:
                intext, reference = social_media(reference_item)
            elif 36 <= reference_item <= 41:
                intext, reference = audio_visual(reference_item)
            elif 42 <= reference_item <= 44:
                intext, reference = image(reference_item)
            else: #other reference types (45 to 54)
                intext, reference = reference_types(reference_item)    
                
                
            os.system('cls')    
            print("The intext reference (where x is the page number if applicable): \n", intext)
            print("The reference itself: \n", reference)
            
        elif choice == '3': 
            user_text = input("Please enter the text that you would like to be read out for you: ")
            language = "en"
            gtts_object = gTTS(text=user_text, lang=language, slow=False)
            gtts_object.save("mytext.mp3")
            os.system("mytext.mp3")
        else: #choice == 4
            #getting the API key which is stored as an environment variable 
            api_key = os.environ.get("openAI_APIKEY")

            #path to the audio file (mytext.mp3)
            audio_file_mytext = "mytext.mp3"

            #URL for the OpenAI API
            url = "https://api.openai.com/v1/audio/transcriptions"

            #seting the headers which will be sent with the request (sending metadata with the request)
            headers = {
                "Authorization": f"Bearer {api_key}"
            }

            #opening the audio file and sending the request to OpenAI's API 
            with open(audio_file_mytext, "rb") as audio_file: #rb stand for read binary which will read any files in binary 
                files = {"file": audio_file}
                data = {"model": "whisper-1"}
                response = requests.post(url, headers=headers, files=files, data=data) #sending request to openAI's API 

            #checking if the request is successful
            if response.status_code == 200:
                #parsing the response JSON
                transcribed_text = response.json()["text"] #text is the key. We are accessing the value of key (API returned JSON object)
                #outputing the transcribed text
                print(transcribed_text)
            else:
                print("Error detected:", response.status_code, response.text)
           
main() #calls main function  
    