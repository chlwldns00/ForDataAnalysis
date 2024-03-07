use sample_mflix;
// MongoDB 검색문 예시연습
db.comments.find().limit(10)
db.movies.find().limit(10)
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
        same_year:{$sum:1}
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
