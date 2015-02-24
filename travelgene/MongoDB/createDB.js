use travelgene
document=({"user_id":"00000001", "user_name":"liuyancheng", "password":"123456", "email":"liuyancheng@gmail.com", "phone":"4125204000", "birth":new Date('May 16, 1991'),"trip_id":["0001","0002"]});
db.user.insert(document)
document=({"user_id":"00000002", "user_name":"shiqiqi", "password":"123456", "email":"shiqiqi@gmail.com", "phone":"4121234567", "birth":new Date('May 16, 1991'),"trip_id":"0001"});
db.user.insert(document)
document=({"user_id":"00000003", "user_name":"zhuangqiankun", "password":"123456", "email":"zhuangqiankun@gmail.com", "phone":"4125204002", "birth":new Date('May 16, 1991'),"trip_id":"0003"});
db.user.insert(document)
document=({"user_id":"00000004", "user_name":"chenglienanjie", "password":"123456", "email":"chenglienanjie@gmail.com", "phone":"4125204000", "birth":new Date('May 16, 1991'),"trip_id":"0004"});
db.user.insert(document)
document=({"user_id":"00000005", "user_name":"xiaolei", "password":"123456", "email":"xiaolei@gmail.com", "phone":"4125204000", "birth":new Date('May 16, 1991'),"trip_id":"0005"});
db.user.insert(document)
document=({"user_id":"00000006", "user_name":"zhanxiaoran", "password":"123456", "email":"zhanxiaoran@gmail.com", "phone":"4125204000", "birth":new Date('May 16, 1991'),"trip_id":"0006"});
db.user.insert(document)
document=({"user_id":"00000007", "user_name":"ranchenyang", "password":"123456", "email":"ranchenyang@gmail.com", "phone":"4125204000", "birth":new Date('May 16, 1991'),"trip_id":"0007"});
db.user.insert(document)
document=({"user_id":"00000008", "user_name":"liuzhiyue", "password":"123456", "email":"liuzhiyue@gmail.com", "phone":"4125204000", "birth":new Date('May 16, 1991'),"trip_id":"0008"});
db.user.insert(document)
document=({"trip_id":"0001","destination":"seattle","depart_date":new Date('May 10, 2014'),"return_date":new Date('May 16, 2014'),"link":["/biz/yogurtland-seattle","/biz/the-elliott-bay-book-company-seattle"]});
db.trip.insert(document)
document=({"trip_id":"0002","destination":"kirkland","depart_date":new Date('Jan 10, 2014'),"return_date":new Date('Jan 16, 2014'),"link":["/biz/brown-bag-cafe-kirkland","/biz/lynns-bistro-kirkland-2"]});
db.trip.insert(document)
