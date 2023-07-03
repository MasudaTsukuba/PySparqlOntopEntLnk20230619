[QueryItem="Q1"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?0 
WHERE {
  ?0 a npdv:ProductionLicence .
}
[QueryItem="Q2"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?0 ?1 ?2 ?3
WHERE { 
  ?0 a npdv:Facility .
  ?0 npdv:name ?1 .
  ?0 npdv:registeredInCountry ?2 . 
  ?0 npdv:idNPD ?3 . 
}
[QueryItem="Q3"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?1 ?2 ?3
WHERE {
  ?0 a npdv:ProductionLicence .
  ?0 npdv:name ?1 .
  ?0 npdv:dateLicenceGranted ?2 .
  ?0 npdv:dateLicenceValidTo ?3 .
}
[QueryItem="Q4"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?1 ?3 ?4
WHERE {
  ?0 a npdv:ProductionLicence .
  ?0 npdv:name ?1 .
  ?0 npdv:licenceLicensee ?2 .
  ?2 npdv:name ?3  .
  ?0 npdv:dateLicenseeValidFrom ?4 . 
}
[QueryItem="Q5"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?0 ?1 ?2 ?3 ?4 ?5  
WHERE {
  ?0 a npdv:FieldReserve .
  ?0 npdv:remainingCondensate     ?1 .
  ?0 npdv:remainingGas            ?2 .
  ?0 npdv:remainingNGL            ?3 .
  ?0 npdv:remainingOil            ?4 .
  ?0 npdv:remainingOilEquivalents ?5  .
  
}