$(function(){
  $('#search_text').keyup(function(){
      var q =  $('#search_text').val()
      // console.log("vlaue = "+q)
      if ((q == '') || (q == null))
      {
        console.log('empty or null')
        $('.result-div').css('display', 'none');

      }
      else
      { 
        console.log('DATA...');
        $('.result-div').css('display', 'block');
        $.ajax({
          type: "GET",
          dataType: "json",
          url: "/books/search/",
          data:{'search_text': q},
          success: searchSuccess,
      });
      }
  });

});


function searchSuccess(data)
{
  // console.log(data)
  var list = "";
  for(i=0; i<data.length; i++)
  { 
    pk = data[i]['pk'];
    title = data[i]['fields']['title'];
    // var url = "{% url 'book_detail'" +pk+"%}"
    // console.log("URL = "+url)

    list += "<a href='"+window.location.href+""+pk+"'> \
    <li class='link list-group-item list-group-item list-group-item-primary' value=''> \
    "+title+"</li></a>"
    
  }
  $('#search_results').html(list)

  $(".link").click(function(){
    text = $(this).text()
    // alert(text);
    $("#search_text").val(text);

  });
}