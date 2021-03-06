wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Seattle.json
wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Bellevue.json
wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Kirkland.json
wget https://raw.githubusercontent.com/TravelGene/Architecture/master/travel/Tripadvisor/Tripadvisor.Redmond.json
mongoimport --db travelgene --collection Seattle --type json --file ./Tripadvisor.Seattle.json --jsonArray
mongoimport --db travelgene --collection Bellevue --type json --file ./Tripadvisor.Bellevue.json --jsonArray
mongoimport --db travelgene --collection Kirkland --type json --file ./Tripadvisor.Kirkland.json --jsonArray 
mongoimport --db travelgene --collection Redmond --type json --file ./Tripadvisor.Redmond.json --jsonArray

mongoimport -h ds031107.mongolab.com:31107 -d travelgene -c <collection> -u <user> -p <password> --file <input file>

mongoimport -h ds031107.mongolab.com:31107 -d travelgene -c Redmond -u travelgene -p genetravel --type json --file ./Tripadvisor.Redmond.json --jsonArray
mongoimport -h ds031107.mongolab.com:31107 -d travelgene -c Bellevue -u travelgene -p genetravel --type json --file ./Tripadvisor.Bellevue.json --jsonArray
mongoimport -h ds031107.mongolab.com:31107 -d travelgene -c Seattle -u travelgene -p genetravel --type json --file ./Tripadvisor.Seattle.json --jsonArray
mongoimport -h ds031107.mongolab.com:31107 -d travelgene -c Kirkland -u travelgene -p genetravel --type json --file ./Tripadvisor.Redmond.json --jsonArray

mongo < createDB.js

db.counters.drop()
db.counters.insert(
   {
      _id: "userid",
      seq: 0
   }
)

function getNextSequence(name) {
   var ret = db.counters.findAndModify(
          {
            query: { _id: name },
            update: { $inc: { seq: 1 } },
            new: true
          }
   );
   return ret.seq;
}

db.Seattle.update(
   { price_range: {$gt:-1} },
   { $set: { place_id: getNextSequence("userid")} },
   {
     multi: true
   }
)
