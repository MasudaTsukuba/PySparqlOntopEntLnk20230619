[QueryItem="q1_book_type"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?book
WHERE{
    ?book rdf:type ex:Book .
}
[QueryItem="q1_book_name"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?book ?book_title
WHERE{
    ?book rdf:type ex:Book ;
        rdfs:label ?book_title .
}
[QueryItem="q2_book_author"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?book ?author
WHERE{
    ?book wdt:P50 ?author .
}
[QueryItem="q1_author_type"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX ex: <http://example.com/>

SELECT  ?author
WHERE{
    ?author a ex:Author .
}
[QueryItem="q1_author_name"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?author ?author_name
WHERE{
    ?author a ex:Author ;
	rdfs:label ?author_name .
}
[QueryItem="q1_genre_type"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?genre
WHERE{
    ?genre rdf:type ex:Genre .
}
[QueryItem="q1_genre_label"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?genre ?genre_label
WHERE{
    ?genre rdf:type ex:Genre ;
        rdfs:label ?genre_label .
}
[QueryItem="q3_cat_author"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?author
WHERE{
    wd:Q35690 wdt:P50 ?author .
}
[QueryItem="q4_bookTitle_authorName"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT DISTINCT ?book ?book_title ?author ?author_name
WHERE{
    ?book wdt:P50 ?author ;
        rdfs:label ?book_title.
    ?author rdfs:label ?author_name .
}
[QueryItem="q4_bookTitle_soseki"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX ex: <http://example.com/>

SELECT DISTINCT ?book ?book_name
WHERE {
    ?book wdt:P50 wd:Q180903 ;
        rdfs:label ?book_name .
}
[QueryItem="q4_book_soseki"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX ex: <http://example.com/>

SELECT DISTINCT ?book
WHERE {
    ?book wdt:P50 wd:Q180903 .
}
[QueryItem="q4_cat_bookTitle"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX ex: <http://example.com/>

SELECT DISTINCT ?book_title
WHERE{
    wd:Q35690 rdfs:label ?book_title.
 }
[QueryItem="q4_cat_bookTitle_authorName"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX ex: <http://example.com/>

SELECT DISTINCT ?book_title ?author ?author_name
WHERE{
    wd:Q35690 wdt:P50 ?author ;
        rdfs:label ?book_title.
    ?author rdfs:label ?author_name .
}
[QueryItem="q5_comics_genreLabel"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX ex: <http://example.com/>

SELECT DISTINCT ?genre_label
WHERE{
    wd:Q1004 rdfs:label ?genre_label.
 }