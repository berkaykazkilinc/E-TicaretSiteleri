var state  = {

    'querySet' : tabledata,
    'page' : 1,
    'rows' : 2, // burda row değilde div mevsuzu olacak zaten

    'window' : 5

}

function pagination(querySet,page,rows){
    var trimStart = (page-1)* rows
    var trimEnd = trimStart + rows 
    
    var trimmedData = querySet.slice(trimStart,trimEnd)

    var pages = Math.ceil(querySet.lenght / rows)

    return{
        'querySet' : trimmedData,
        'pages' : page
    }
}