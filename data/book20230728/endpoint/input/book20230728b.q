[QueryItem="q1_book_type"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?book
WHERE{
    ?book rdf:type ex:Book .
}
[QueryItem="q1_book_title"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?book ?book_title
WHERE{
    ?book rdf:type ex:Book ;
        rdfs:label ?book_title .
}
[QueryItem="q1_author_type"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/>

SELECT ?author
WHERE{
    ?author rdf:type ex:Author .
}