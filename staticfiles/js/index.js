var selectList = [];
var whereList = [];

$(document).ready(function () {

    selectList=[];
    whereList = [];
    selectList.push(["id","id"])
    showSelectQuery();

    $("form").on("submit", function () {
        $("#loadingModal").show();
    });
    $(".close").on("click", function () {
        $("#loadingModal").hide();
    });
    $(window).on("click", function (event) {
        if ($(event.target).is("#loadingModal")) {
            $("#loadingModal").hide();
        }
    });

    $('.select_query').change(function() {
        const checkboxName = $(this).attr('name');
        const isChecked = $(this).is(':checked');

        const query_matching = {
            "highway": "tags['highway']",
            "maxspeed": "tags['maxspeed']",
            "lane": "tags['lanes']",
            "oneway": "tags['oneway']",
            "license": "tags['license']"
        };

        const key = checkboxName in query_matching ? checkboxName : null;
        const val = key ? query_matching[key] : "";

        if (isChecked && key) {
            selectList.push([key, val]);
        } else if (!isChecked && key) {
            selectList = selectList.filter(item => item[0] !== key);
        } else {
            console.log('undefined checkbox');
        }
    
        showSelectQuery();
    });

    $(".where_rdo_query").change(function(){
        const itemName = $(this).attr('name');
        const itemValue = $(this).val();

        let val = "";

        switch(itemName){
            case "cond_type":
                val = `kind='${itemValue}'`;               
                break;
            case "cond_oneway":
                if(itemValue == 'yes'){
                    val = `tags['oneway'] in ('-1', '${itemValue}')`;    
                }
                else if(itemValue == 'no'){
                    val = `tags['oneway'] = '${itemValue}'`;  
                }
                break;
        }

        whereList = whereList.filter(item => item[0] !== itemName);
        if(val != ""){
            whereList.push([itemName,val]);
        }
        showWhereQuery();
    });

    $(".where_txt_query").on('blur', function(){
        const itemName = $(this).attr('name');
        const itemValue = $(this).val();

        const condition_matching = {
            "cond_amenity": `tags['amenity']${itemValue}`,
            "cond_brand": `tags['brand']${itemValue}`,
            "cond_state": `tags['addr:state'] = '${itemValue}'`,
            "cond_city": `tags['addr:city'] = '${itemValue}'`,
            "cond_street": `tags['addr:street'] = '${itemValue}'`,
            "cond_housenumber": `tags['addr:housenumber'] = '${itemValue}'`,
            "cond_postcode": `tags['addr:postcode'] = '${itemValue}'`,
            "cond_others": `${itemValue}`
        };

        const val = condition_matching[itemName] || "";

        whereList = whereList.filter(item => item[0] !== itemName);

        if(itemValue){
            whereList.push([itemName,val]);
        }
        showWhereQuery();
    });

    $('#select_others').on('blur', function() {

        const key = 'other';
        const val = $(this).val();
        selectList = selectList.filter(item => item[0] !== key);

        if(val){
            selectList.push([key,val]);
        }
        showSelectQuery();
    });
    $('#chk_highway').change(function () {
        $('input[name="cond_highway"]').prop('checked', this.checked);
    });
});

function showSelectQuery(){
    const query = selectList.map(lst => lst[1]).join(",");
    $("#select_sql").val(query);
}

function showWhereQuery(){
    const query = whereList.map(lst => lst[1]).join(" AND ");
    $("#where_sql").val(query);
}