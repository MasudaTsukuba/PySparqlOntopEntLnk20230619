[QueryItem="Q1"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0
WHERE
{
	?var0  rdf:type :StockExchangeMember
}order by ?var0
[QueryItem="Q2"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 ?var1
WHERE
{
	?var0  rdf:type :Person .
	?var0  :hasStock ?var1  .
	?var1  rdf:type :Stock .
}
[QueryItem="Q3"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 ?var1 ?var2
WHERE
{
	?var1  :hasStock ?var2  .
	?var2  rdf:type :Stock .
	?var1  rdf:type :Company .
	?var0  :belongsToCompany ?var1  .
	?var0  rdf:type :FinantialInstrument .
}
[QueryItem="Q4"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 ?var1 ?var2
WHERE
{
	?var0  rdf:type :Person .
	?var0  :hasStock ?var1  .
	?var1  rdf:type :Stock .
	?var1  :isListedIn ?var2  .
	?var2  rdf:type :StockExchangeList
}
[QueryItem="Q5"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 ?var1 ?var2 ?var3
WHERE
{
	?var0  rdf:type :FinantialInstrument .
	?var0  :belongsToCompany ?var1  .
	?var1  rdf:type :Company .
	?var1  :hasStock ?var2  .
	?var2  rdf:type :Stock .
	?var1  :isListedIn ?var3  .
	?var3  rdf:type :StockExchangeList
}
[QueryItem="Q2_hasStock"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 ?var1
WHERE
{
	?var0  :hasStock ?var1  .
}
[QueryItem="Q2_Stock"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var1
WHERE
{
	?var1  rdf:type :Stock .
}
[QueryItem="Q2_Person"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 
WHERE
{
	?var0  rdf:type :Person .
} ORDER BY ?var0
[QueryItem="Q2_hasStock_Stock"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.owl-ontologies.com/Ontology1207768242.owl#>
SELECT DISTINCT ?var0 ?var1
WHERE
{
	?var0  :hasStock ?var1  .
	?var1  rdf:type :Stock .
}