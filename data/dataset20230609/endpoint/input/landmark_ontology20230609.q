[QueryItem="3_q1"]
PREFIX pred: <http://example.com/predicate/>

SELECT ?building_id ?country_id
WHERE {
?building_id pred:country ?country_id.
}
[QueryItem="3_q2"]
PREFIX ex: <http://example.com/building/id/>
PREFIX wd: <https://www.wikidata.org/wiki/> 
PREFIX pred: <http://example.com/predicate/>

SELECT ?building_id ?country_id
WHERE {
?building_id pred:country ?country_id.
FILTER( ?building_id != ex:899b )
}
[QueryItem="3_q3"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/building/id/>
PREFIX wd: <https://www.wikidata.org/wiki/> 
PREFIX pred: <http://example.com/predicate/>

SELECT ?building_id ?name ?country_id
WHERE {
?building_id pred:country ?country_id.
?building_id rdfs:label ?name.
FILTER( ?building_id != ex:899b )
}
[QueryItem="query_with_OR_in_filter20230615"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/building/id/>
PREFIX ex_country: <http://example.com/country/id/>
PREFIX wd: <https://www.wikidata.org/wiki/>
PREFIX schema: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pred: <http://example.com/predicate/>

SELECT ?building_id ?name ?country_id
WHERE {
?building_id pred:country ?country_id .
?building_id rdfs:label ?name.
FILTER( (?building_id = ex:899b || ?building_id = ex:1521b ) && ?country_id = ex_country:79 )
}