var emptyRow = "<tr><td colspan='5' class='text-center'> No Records Available</td></tr>";
        var emptyNewRow = "<tr class='trNewRow'>"; 
        emptyNewRow = emptyNewRow + "    <td class='tdDate'>";
        emptyNewRow = emptyNewRow + "        <input type='date' class='form-control txtDate' placeholder='mm/dd/yyyy'/>";
        emptyNewRow = emptyNewRow + "    </td>";
        emptyNewRow = emptyNewRow + "    <td class='tdActivity'>";
        emptyNewRow = emptyNewRow + "        <input type='text' class='form-control txtActivity' placeholder='Enter Activity'/>";
        emptyNewRow = emptyNewRow + "    </td>";
        emptyNewRow = emptyNewRow + "    <td class='tdRemarks'>";
        emptyNewRow = emptyNewRow + "        <input type='text' class='form-control txtRemarks' placeholder='Enter Remarks'/>";
        emptyNewRow = emptyNewRow + "    </td>";
        emptyNewRow = emptyNewRow + "    <td class='tdStatus'>";
        emptyNewRow = emptyNewRow + "        <input type='text' class='form-control txtStatus' placeholder='Complete | Ongoing'/>";
        emptyNewRow = emptyNewRow + "    </td>";
        emptyNewRow = emptyNewRow + "    <td class='tdAction' style='text-align: center;'>";
        emptyNewRow = emptyNewRow + "        <button class='btn btn-sm btn-success btn-c btn-save'> Save</button>";
        emptyNewRow = emptyNewRow + "        <button class='btn btn-sm btn-success btn-c btn-cancel'> Cancel</button>";
        emptyNewRow = emptyNewRow + "    </td>";
        emptyNewRow = emptyNewRow + "</tr>";

        var rowButtons ="<button class='btn btn-success btn-sm btn-c btn-edit' style='text-align: center;'> Edit </button>  <button class='btn btn-danger btn-sm' style='text-align: center;'> Delete </button> ";
        var rowUpdateButtons ="<button class='btn btn-success btn-sm btn-c btn-save'style='text-align: center;' > Update </button>  <button class='btn btn-danger btn-sm btn-save' style='text-align: center;'> Cancel </button> ";

        $(document).ready(function () {
            debugger;
            $("#tblData tbody").append(emptyRow); // adding empty row on page load 
            
            $("#btnAdd").click(function () { 
                debugger;
                if ($("#tblData tbody").children().children().length == 1) {
                    $("#tblData tbody").html("");
                }
                debugger;
                $("#tblData tbody").append(emptyNewRow); // appending dynamic string to table tbody
            });
            
            $('#tblData').on('click', '.btn-save', function () {
                const date =  $(this).parent().parent().find(".txtDate").val();
                $(this).parent().parent().find(".tdDate").html(""+date+""); 
                const activity =  $(this).parent().parent().find(".txtActivity").val();
                $(this).parent().parent().find(".tdActivity").html(""+activity+"");
                const remarks =  $(this).parent().parent().find(".txtRemarks").val();
                $(this).parent().parent().find(".tdRemarks").html(""+remarks+"");
                const status =  $(this).parent().parent().find(".txtStatus").val();
                $(this).parent().parent().find(".tdStatus").html(""+status+"");
                $(this).parent().parent().find(".tdAction").html(rowButtons);
            });
             
            
            $('#tblData').on('click', '.btn-danger', function () { // registering function for delete button  
                $(this).parent().parent().remove();
                if ($("#tblData tbody").children().children().length == 0) {
                    $("#tblData tbody").append(emptyRow);
                }
            });
            

            $('#tblData').on('click', '.btn-cancel', function () { 
                $(this).parent().parent().remove();
            });
            $('#tblData').on('click', '.btn-edit', function () { 
                const date =$(this).parent().parent().find(".tdDate").html();
                $(this).parent().parent().find(".tdDate").html("<input type='date' value='"+date+"' class='form-control txtDate' placeholder='mm/dd/yyyy'/>"); 

                const activity =$(this).parent().parent().find(".tdActivity").html();
                $(this).parent().parent().find(".tdActivity").html("<input type='text' value='"+activity+"' class='form-control txtActivity' placeholder='Enter Activity'/>"); 

                const remarks =$(this).parent().parent().find(".tdRemarks").html();
                $(this).parent().parent().find(".tdRemarks").html("<input type='text' value='"+remarks+"' class='form-control txtRemarks' placeholder='Enter Remarks'/>"); 
                
                const status =$(this).parent().parent().find(".tdStatus").html();
                $(this).parent().parent().find(".tdStatus").html("<input type='text'  value='"+status+"' class='form-control txtStatus' placeholder='Complete | Ongoing'/>");
                       
                $(this).parent().parent().find(".tdAction").html(rowUpdateButtons);
                 
                
            });
        });