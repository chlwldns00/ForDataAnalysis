use sample_mflix;
// MongoDB 검색문 예시연습
db.comments.find().limit(10)
db.movies.find().limit(10)
db.comments.find().limit(10)
db.movies.find(
{},{cast:1}
).limit(10)

//group화 한 documents를 리스트 형태로 출력
db.movies.aggregate([
 {
   $group: {
     _id: "$year",
     titles: { $push: "$title" }
   }
 }
]);


//실습문제 part1

//연습문제 1 2000년 이후로 출시된 영화의 수는 얼마인가요? <year type 수치비교 가능?>
db.movies.aggregate([
    {$match: {year: {$gt:2000}}},
    {$count:"2000after"}
])

//연습문제 2 각 연도별로 출시된 영화의 수는 어떻게 되나요?
db.movies.aggregate([
{
    $group: {
        _id:"$year",
        same_year:{$sum:1}
    }
}
])

//3. 가장 많은 영화가 출시된 연도는 언제인가요?
db.movies.aggregate([
    {
    $group: {
        _id:"$year",
        same_year:{$sum:1} //group by having 
    }
    },
    {$sort :{"same_year":-1}},
    {$limit:1}

]);
// 4. 각 연도별 평균 영화 러닝타임은 어떻게 되나요?
db.movies.aggregate([
{
    $group:{
    
        _id:"$year",
        same_year_avg_runtime:{$avg:"$runtime"}
    }
}
]);
// 5. 가장 러닝타임이 긴 영화는 어떤 영화인가요?
db.movies.aggregate([
{
    $sort:{runtime:-1}
},
{$limit:1}
])

//6. 각 영화 장르별 평균 IMDB 평점은 어떻게 되나요?(장르 속성이 리스트 타입이므로 $unwind 파이프라인으로 각각의 요소들을 풀어줘야함
db.movies.aggregate([
{$unwind:"$genres"},
   
     {
       $group: {
         _id: "$genres",
         averageRating: { $avg: "$imdb.rating" }
       }
     }
   ]);

// 7. 각 연도별 영화 제목의 평균 길이는 어떻게 되나요?
db.movies.aggregate([
{$match: { plot: { $ne: null } }},
{
    $group: {
        _id:"$year",
        name_len_avg:{$avg:{$strLenCP:{$toString:"$plot"}}}  //$plot 은 str 타입같은데 왜 안되는거
    }
}])

// 8. 각 연도별로 가장 먼저 출시된 영화의 제목은 무엇인가요?

db.movies.aggregate([
     {$sort:{year:1,released:1}},
     {
       $group: {
         _id: "$year",
         first_movie:{$first:"$title"}
         
       }
     },
     {$sort:{_id:1}}
  
   ]);
   
// 9. 각 연도별로 가장 마지막에 출시된 영화의 제목은 무엇인가요?

db.movies.aggregate([
     {$sort:{year:1,released:1}},
     {
       $group: {
         _id: "$year",
         first_movie:{$last:"$title"}
         
       }
     },
     {$sort:{_id:1}}
  
   ]);


// 10. 각 연도별로 고유한 영화 장르는 어떻게 되나요?
db.movies.aggregate([

    {$unwind:"$genres"},
    {
        $group: {
            _id:"$year",
            varietyofGenres:{$addToSet:"$genres"}
              
        }
    },
    {$sort:{_id:1}}
]
)

//////////////////////////////////////////////////////////////////////////////
//실습문제 part2


//1-1. 추가적으로 댓글끝에 (날짜) 붙이기 
db.comments.aggregate([
    { 
        $project: {
            name:1,
            text: 1,
            date: 1,
            comment_info: { $concat: [ " name:","$name","\n comment:" ,{ $toString: "$text" }, "\n date:",{ $toString: "$date" }] }
        }
    }
]);
db.comments.aggregate([{$limit:20}])

//1-2 각 영화의 제목과 해당 영화에 달린 댓글들을 출력하세요
db.movies.aggregate([     
   {
      $lookup:
        {
          from: "comments",   
          localField: "_id",   
          foreignField: "movie_id",   
          as: "movie_info"  
        }
   },
   {
       $project: {
           _id:0,
           title:1,
           movie_info: {
                $map: {
                  input: "$movie_info",
                  as: "comment",
                  in: "$$comment.text"
              }
           }
           
       }
   },
   
   {$skip:5},
   {$limit:5}
])
// 1-3 조인결과 출력 (조인과 피조인 컬럼 하나씩 출력)
db.movies.aggregate([      //중간중간 null값이 조인된 이유는, movies 컬렉션에서는 있는 movie_id가 comments컬렉션에는 없을수도 있어서 허공에 떠있는 조인느낌인것.
   {
      $lookup:
        {
          from: "comments",   
          localField: "_id",   
          foreignField: "movie_id",   
          as: "movie_info"  
        }
   },
   {
       $project: {
           _id:0,
           title:1,
           movie_info:1
       }
   },
   {$limit:5}
   ])    


// 2. 평점이 가장 높은 영화의 제목과 평점을 출력하세요
db.movies.aggregate([
    { $match: { "imdb.rating": { $ne: ""} } }, //$ne:null or ""
    { $sort: { "imdb.rating": -1} },
    { $limit: 1},
    { $project: { _id: 0, title: 1, "imdb.rating": 1} }
])

//3. 각 장르별로 평균 평점이 가장 높은 장르와 평균 평점을 출력하세요.
db.movies.aggregate([
{ $unwind:"$genres"},
{
    $group: {  //group by genres
        _id:"$genres",
        avg_rating:{$avg:"$imdb.rating"}
    }
},
{$sort:{avg_rating:-1}}, //sort desc
{$limit:1},
{  
    $project:{  //select avg(imdb.ratings)
        _id:1,
        avg_rating:1
    }
}

    
])

//4. 개봉 연도별로 평균 러닝타임이 가장 짧은 영화의 개봉 연도와 평균 러닝타임을 출력하세요.
db.movies.aggregate([
    { $group: 
        { _id: "$year", 
          avgRuntime: { $avg: "$runtime"} 
        } 
    },
    { $sort: { avgRuntime: 1} },
    { $limit: 1},
    { $project: { _id: 0, year: "$_id", avgRuntime: 1} } //가장 짧은 영화의 
])

//5. 각 국가별로 가장 많은 영화를 제작한 감독과 그 감독의 영화 수를 출력하세요.
db.movies.aggregate([
    {$unwind:"$countries"},
    {$unwind:"$directors"},
    {
        $group:{
            _id:{country:"$countries",director:"$directors"},  //여기서 2개의 컬럼이 그룹바이 된게 어캐된 형태이지 =>국가가 같고, 감독이 같은것끼리 모아놓은후(리스트 형태로 모아놓음)[usa,woodyallen] 그것들 컬럼의 합
            sum:{$sum:1} //$sum:1 이나 그냥 count는 단순 튜플수를 세는것이고 어떤컬럼을 세는 조건을 걸려면 match{조건} 후 count 이게 맞는거같다
        }
    },
    {
        $sort:{sum:-1}
    },
    {
        $project: {
            _id:0,
            director:"$_id.director", //group by하거나 look up 해서 합쳐져서 리스트로 만들어진 것중 하나에 참조 하려면 "$전체.속성"
            sum:1
        }
    },
    {
        $limit:1
    }        
])

//6. 각 연도별로 가장 높은 평점을 받은 영화의 제목과 평점을 출력하세요.
db.movies.aggregate([
    {$match:{"imdb.rating":{$ne:""}}}, // 레이팅 값이 ""인것들 제외하고 검색
    { $sort: { "year": 1, "imdb.rating": -1 } }, //
    {
        $group: {
            _id: "$year",
            title: { $first: "$title" },
            maxRating: { $first: "$imdb.rating" }
        }
    },
    { $project: { _id: 0, year: "$_id", title: 1, maxRating: 1 } }
])


//7. 각 장르별 영화 갯수를 영화 갯수가 가장 많은 순으로 출력하세요.
db.movies.aggregate([
    { $unwind: "$genres" },
    { $group: 
        { _id: "$genres", 
            count: { $sum: 1} 
        } 
    },
    { $sort: { count: -1 } },
    { $project: { _id: 0, genre: "$_id", movieCount: "$count" } }
])

//8.영화 감독별로 평균 평점이 가장 높은 감독과 그 감독의 평균 평점을 출력하세요.
db.movies.aggregate([
  { $unwind: "$directors" },
  { $group: 
      { _id: "$directors", avgRating: { $avg: "$imdb.rating" } } },
  { $sort: { avgRating: -1 } },
  { $limit: 1 },
  { $project: { _id: 0, director: "$_id", avgRating: 1 } }
]);


//9.장르별로 평균 러닝타임이 가장 긴 장르와 그 장르의 평균 러닝타임을 출력하세요.
db.movies.aggregate([
  { $unwind: "$genres" },
  { $group: { _id: "$genres", avgRuntime: { $avg: "$runtime" } } },
  { $sort: { avgRuntime: -1 } },
  { $limit: 1 },
  { $project: { _id: 0, genre: "$_id", avgRuntime: 1 } }
]);


//10. 각 영화의 제목과 해당 영화에 대해 댓글을 남긴 사용자들을 출력하세요.
db.movies.aggregate([
  { 
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "movie_id",
      as: "movie_info"
    }
  },
  { 
    $project: { 
      _id: 0, 
      title: 1, 
      users: "$movie_info.name" 
    } 
  },
  {$limit:10}
  ])