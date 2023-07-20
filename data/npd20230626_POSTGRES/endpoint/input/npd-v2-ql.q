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
} ORDER BY ?var0
[QueryItem="Q3"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?var0 ?var1 ?var2 ?var3
WHERE {
  ?var0 a npdv:ProductionLicence .
  ?var0 npdv:name ?var1 .
  ?var0 npdv:dateLicenceGranted ?var2 .
  ?var0 npdv:dateLicenceValidTo ?var3 .
} ORDER BY ?var0
[QueryItem="Q4"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?var0 ?var1 ?var2 ?var3 ?var4
WHERE {
  ?var0 a npdv:ProductionLicence .
  ?var0 npdv:name ?var1 .
  ?var0 npdv:licenceLicensee ?var2 .
  ?var2 npdv:name ?var3  .
  ?var0 npdv:dateLicenseeValidFrom ?var4 .
} ORDER BY ?var0
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
  
}ORDER BY ?var0
[QueryItem="Q3b"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?licence_id ?licence_name
WHERE {
  ?licence_id a npdv:ProductionLicence .
  ?licence_id npdv:name ?licence_name .
}ORDER BY ?licence_id
[QueryItem="npd_q01"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?licenceURI ?interest ?date
WHERE {
  ?licenceURI a npdv:ProductionLicence .

  [ ] a npdv:ProductionLicenceLicensee ;
  npdv:dateLicenseeValidFrom ?date ;
  npdv:licenseeInterest ?interest ;
  npdv:licenseeForLicence ?licenceURI .
  FILTER(?date > "1979-12-31"^^xsd:date)
}
[QueryItem="npd_q08"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?year ?m ?g ?o
WHERE {
  [ npdv:productionYear ?year ;
    npdv:productionMonth ?m ;
    npdv:producedGas     ?g ;
    npdv:producedOil     ?o
  ]
  FILTER (?year > 1999)
  FILTER(?m >= 1 && ?m <= 6 )
}
[QueryItem="npd_q01b2"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?s ?licenceURI
WHERE {
  ?licenceURI a npdv:ProductionLicence .

  ?s a npdv:ProductionLicenceLicensee .
}
[QueryItem="nps_q08_order"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX npdv: <http://sws.ifi.uio.no/vocab/npd-v2#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?s ?year ?m ?g ?o
WHERE {
  ?s
    npdv:productionYear ?year ;
    npdv:productionMonth ?m ;
    npdv:producedGas     ?g ;
    npdv:producedOil     ?o .
  FILTER (?year > 1999)
  FILTER(?m >= 1 && ?m <= 6 )
}ORDER BY ?s ?year