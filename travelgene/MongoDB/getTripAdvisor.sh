wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Seattle.json
wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Bellevue.json
wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Kirkland.json
wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Redmond.json
mongoimport --db travelgene --collection seattle --type json --file ./Tripadvisor.Seattle.json --jsonArray
mongoimport --db travelgene --collection bellevue --type json --file ./Tripadvisor.Bellevue.json --jsonArray
mongoimport --db travelgene --collection kirkland --type json --file ./Tripadvisor.Kirkland.json --jsonArray
mongoimport --db travelgene --collection redmond --type json --file ./Tripadvisor.Redmond.json --jsonArray
