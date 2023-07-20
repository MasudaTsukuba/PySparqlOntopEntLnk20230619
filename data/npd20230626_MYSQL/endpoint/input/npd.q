[QueryItem="Q1"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?var0
WHERE {
  ?var0 a npdv:ProductionLicence .
}
[QueryItem="Q2"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?var0 ?var1 ?var2 ?var3
WHERE { 
  ?var0 a npdv:Facility .
  ?var0 npdv:name ?var1 .
  ?var0 npdv:registeredInCountry ?var2 .
  ?var0 npdv:idNPD ?var3 .
}
[QueryItem="Q3"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?var1 ?var2 ?var3
WHERE {
  ?var0 a npdv:ProductionLicence .
  ?var0 npdv:name ?var1 .
  ?var0 npdv:dateLicenceGranted ?var2 .
  ?var0 npdv:dateLicenceValidTo ?var3 .
}
[QueryItem="Q4"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?var1 ?var3 ?var4
WHERE {
  ?var0 a npdv:ProductionLicence .
  ?var0 npdv:name ?var1 .
  ?var0 npdv:licenceLicensee ?var2 .
  ?var2 npdv:name ?var3  .
  ?var0 npdv:dateLicenseeValidFrom ?var4 .
}
[QueryItem="Q5"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?var0 ?var1 ?var2 ?var3 ?var4 ?var5
WHERE {
  ?var0 a npdv:FieldReserve .
  ?var0 npdv:remainingCondensate     ?var1 .
  ?var0 npdv:remainingGas            ?var2 .
  ?var0 npdv:remainingNGL            ?var3 .
  ?var0 npdv:remainingOil            ?var4 .
  ?var0 npdv:remainingOilEquivalents ?var5  .
  
}