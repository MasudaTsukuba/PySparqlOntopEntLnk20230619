[QueryItem="q1"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX onto: <http://example.com/ontology/>
PREFIX pred: <http://example.com/predicate/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?hotel_name ?country_name
WHERE {
    ?s rdf:type onto:Hotel.
    ?s rdfs:label ?hotel_name.
    ?s pred:country ?country_id.
    ?country_id pred:country_name ?country_name.
}
[QueryItem="q1_country_pred"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

PREFIX ex: <http://example.com/>
PREFIX onto: <http://example.com/ontology/>
PREFIX pred: <http://example.com/predicate/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_description: <http://example.com/predicate/country_description>

SELECT ?p ?o
WHERE {
    <http://example.com/country/id/45> ?p ?o.
}
[QueryItem="q1_hotel_country_id"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

PREFIX ex: <http://example.com/ontology/>
PREFIX predicate: <http://example.com/predicate/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_description: <http://example.com/predicate/country_description>

SELECT ?s ?name ?country_id
WHERE {
    ?s rdf:type ex:Hotel.
    ?s rdfs:label ?name.
    ?s predicate:country ?country_id.
} order by ?s