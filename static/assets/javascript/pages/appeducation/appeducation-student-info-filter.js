
$.ajaxSetup({ 
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    } 
});

$('#id_class_id').change( function(){
    $.when(student_filter()).then(
    filter_classlist()
   );
   
})
$('#id_class_group_id').change( function(){
    $.when(student_filter()).then(
    filter_classlist()
   );
   
})

function student_filter(){
    class_id=document.getElementById('id_class_id').value
    class_group_id=document.getElementById('id_class_group_id').value
    subject_id=document.getElementById('subject-list').value
    postdata={
        class_id:class_id,
        class_group_id:class_group_id,
        subject_id:subject_id
    }
$.ajax({
    url: '/edu-student-info-filtered',
    data: postdata,
    type: 'POST',
    success: function (data) {
        document.getElementById('table-data').innerHTML=data
    }
})
}


function filter_classlist() {
    class_id=document.getElementById('id_class_id').value
    class_group_id=document.getElementById('id_class_group_id').value
    // subject-list
    $.ajax({
        url: "/apiedu-subject-list-api/?class_id="+class_id+"&class_group_id="+class_group_id,
        type: 'get',
        dataType: 'json',
        success: function (data) {
            $("#subject-list option").remove();
            $("#subject-list").append('<option value="">------------</option>');
            data.forEach(element => {
                $("#subject-list").append('<option value="'+element.subject_id+'">'+element.subject_name+'</option>');
            });
            console.log(data)
        }
    })
}

// total-mark-intable
function ShowTotalmark(exam_id){
    $.ajax({
        url: "/apiedu-exam-setup-api/?exam_id="+exam_id,
        type: 'get',
        dataType: 'json',
        success: function (data) {
            $('.total-mark-intable').text(data[0].total_exam_marks)
        }
    })
}

function insertMark(value,roll){
    exam_id=document.getElementById('exam-list').value
    subject_id=document.getElementById('subject-list').value
    total_mark=document.getElementById('total_mark'+roll).textContent
    if(exam_id && subject_id && total_mark){
    postdata={
        exam_id:exam_id,
        subject_id:subject_id,
        total_exam_marks:total_mark,
        obtain_marks:value,
        student_roll:roll
    }
        $.ajax({
            url: '/edu-insert-student-mark',
            data:postdata,
            type: 'POST',
            success: function (data) {
                $('#greate_point'+roll).text(data.grade_point)
                $('#greate'+roll).text(data.result_grade)
            }
        })
    }
}



console.log("Hello")
console.log("Hello")