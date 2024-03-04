//4.1 연습문제
db.createCollection('users') //capped 같은 옵션을 붙일수있다.
db.users.insertMany( 
   [
    { name:"David", age:45, address:"서울" },
	{ name:"DaveLee", age:25, address:"경기도" },
	{ name:"Andy", age:50, hobby:"골프", address:"경기도" },
	{ name:"Kate", age:35, address:"수원시" },
	{ name:"Brown", age:8 }
   ]
) ;
db.users.find()