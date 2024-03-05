//mongodb collection생성
db.createCollection('users',{ capped : true, max : 5000 }) //capped 같은 옵션을 붙일수있다.
db.users.insertMany( 
   [
    { name:"David", age:45, address:"서울" },
	{ name:"DaveLee", age:25, address:"경기도" },
	{ name:"Andy", age:50, hobby:"골프", address:"경기도" },
	{ name:"Kate", age:35, address:"수원시" },
	{ name:"Brown", age:8 }
   ]
) ;
//Read 예제

//4.2-1 users Collection 에서 name 이 DaveLee 인 Document의 name, age, address, _id 출력<br>
//users Collection 에서 name 가 Kate 인 Document의 name, age, address 출력<br>
db.users.find( 
   {name:'DaveLee'},
   {name:1, age:1,_id:0}
);
db.users.find(
{name:'kate'},
{name:1,age:1,address:1,_id:0}
)

//4-2.2 다음 Document 데이터 넣기
//   - age 가 20 보다 큰 Document 의 name 만 출력하기<br>
//   - age 가 50 이고 address 가 경기도 인 Document 의 name 만 출력하기
db.users.find(

{age:{$gt:20}},
{name:1,_id:0}

);
db.users.find(
{age:50, address:"경기도"},
{name:1,_id:0}
);

//4-2-3 users Collection 에서 name 가 Brown 이거나, age가 35인 Document 의 모든 필드 출력
db.users.find(
{$or:[{name:'Brown'},{age:35}]}

)

