[QueryItem="all"]
select ?s ?p ?o where {?s ?p ?o. }
[QueryGroup="hotel"] @collection [[
[QueryItem="hotel_name_and_comment"]
PREFIX onto: <http://example.com/ontology/>
select * where {
?id rdf:type onto:Hotel.
?id rdfs:label ?name.
?id rdf:comment ?comment.
}
[QueryItem="hotel_country_name_and_comment"]
PREFIX onto:<http://example.com/ontology/>

select * where {
?s rdf:type onto:Hotel.
?s rdfs:label ?hotel_name.
?s <http://example.com/predicate/country> ?id.
?id <http://example.com/predicate/country_name> ?name;
<http://example.com/predicate/country_description> ?comment.
}
[QueryItem="hotel_id"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

PREFIX ex: <http://example.com/ontology/>
select * where {
?id ?p ex:Hotel.
}LIMIT 5
]]
[QueryGroup="museum"] @collection [[
[QueryItem="museum_name_and_comment"]
PREFIX onto: <http://example.com/ontology/>
select * where {
?id rdf:type onto:Museum.
?id rdfs:label ?name.
?id rdf:comment ?description.
}
[QueryItem="museum_country_name_and_comment"]
PREFIX ex:<http://example.com/ontology/>

select * where {
?s rdf:type ex:Museum.
?s rdfs:label ?museum_name.
?s <http://example.com/predicate/country> ?id.
?id <http://example.com/predicate/country_name> ?name;
<http://example.com/predicate/country_description> ?comment.
} LIMIT 5
]]
[QueryGroup="build"] @collection [[
[QueryItem="build_name_and_comment"]
PREFIX onto: <http://example.com/ontology/>
select ?id ?name ?comment where {
?id rdf:type onto:Building.
?id rdfs:label ?name.
?id rdf:comment ?comment.
}
[QueryItem="build_country_name_and_comment"]
PREFIX ex:<http://example.com/ontology/>

select ?s ?build_name ?id ?name ?comment where {
?s rdf:type ex:Building.
?s rdfs:label ?build_name.
?s <http://example.com/predicate/country> ?id.
?id <http://example.com/predicate/country_name> ?name;
<http://example.com/predicate/country_description> ?comment.
}
]]
[QueryGroup="heritage"] @collection [[
[QueryItem="heritage_name_and_comment"]
PREFIX onto: <http://example.com/ontology/>
select * where {
?id rdf:type onto:Heritage.
?id rdfs:label ?name.
?id rdf:comment ?comment.
}
[QueryItem="heritage_country_name_and_comment"]
PREFIX onto:<http://example.com/ontology/>
PREFIX pred: <http://example.com/predicate/>
select ?s ?heritage_name ?id ?name ?comment where {
?s rdf:type onto:Heritage.
?s rdfs:label ?heritage_name.
?s pred:country ?id.
?id pred:country_name ?name;
pred:country_description ?comment.
}
]]
[QueryGroup="20230210sato"] @collection [[
[QueryItem="q1"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX onto: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdf:type onto:Hotel.
    ?s rdfs:label ?name.
    ?s country: ?c_id.
    ?c_id country_name: ?cname.
}
[QueryItem="q2"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX onto: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdf:type onto:Museum.
    ?s rdfs:label ?name.
    ?s country: ?c_id.
    ?c_id country_name: ?cname.
    FILTER(?cname = 'United Kingdom')
}
[QueryItem="q3a"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX onto: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdfs:label ?name.
    ?s country: ?c_id.
    ?c_id country_name: ?cname.
    FILTER(?cname = 'United Kingdom')
}
[QueryItem="q3b"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX onto: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?name ?cname
WHERE {
    ?s rdfs:label ?name.
    ?s country: ?c_id.
    ?c_id country_name: ?cname.
    FILTER(?cname = 'United Kingdom')
}
[QueryItem="q4"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/>
PREFIX onto: <http://example.com/ontology/>
PREFIX country: <http://example.com/predicate/country>
PREFIX pred: <http://example.com/predicate/>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdf:type onto:Museum.
    ?s rdfs:label ?name.
    ?s pred:country ?c_id.
    ?c_id pred:country_name ?cname.
}
[QueryItem="q5"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX onto: <http://example.com/ontology/>
PREFIX pred: <http://example.com/predicate/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdfs:label ?name.
    ?s pred:country ?c_id.
    ?c_id pred:country_name ?cname.
}
[QueryItem="q6"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX onto: <http://example.com/ontology/>
PREFIX pred: <http://example.com/predicate/>
PREFIX country: <http://example.com/predicate/country>
PREFIX country_name: <http://example.com/predicate/country_name>
PREFIX country_comment: <http://example.com/predicate/country_comment>

SELECT ?s ?name ?cname
WHERE {
    ?s rdf:type onto:Heritage.
    ?s rdfs:label ?name.
    ?s pred:country ?c_id.
    ?c_id pred:country_name ?cname.
    FILTER(?cname = 'Japan')
}
]]
[QueryGroup="landmark"] @collection [[
[QueryItem="landmark_name_and_comment"]
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

PREFIX onto: <http://example.com/ontology/>
select * where {
?id rdf:type onto:Landmark.
?id rdfs:label ?name .
?id rdf:comment ?comment.
}LIMIT 10
]]