from django.shortcuts import render
import duckdb
from .forms import PbfViewerForm


def home(request):
    form = PbfViewerForm()
    return render(request, 'pbf_viewer/index.html', {'form':form})   

def load_data(request):

    if request.method == 'GET':
        return render(request, 'pbf_viewer/index.html', {'form':PbfViewerForm()})   
    
    if request.method == 'POST' :

        form = PbfViewerForm(request.POST)

        if not form.is_valid():
            return render(request, 'pbf_viewer/index.html', {'form':PbfViewerForm()})   
        
        header, data, query = None, None, None
        error_message = None
        try:
            query = ""
            select_sql = request.POST.get('select_sql')
            where_sql = request.POST.get('where_sql')
            from_sql = request.POST.get('from_sql')
            limit = request.POST.get('cond_limit')
            if limit == "":
                limit = int(100)
            
            if where_sql == "":
                query = f"SELECT {select_sql} FROM '{from_sql}' limit {limit} ;"
            else:
                query = f"SELECT {select_sql} FROM '{from_sql}' WHERE {where_sql} limit {limit} ;"
            
            with duckdb.connect() as con:
                con.install_extension("spatial")
                con.load_extension("spatial")
                
                result = con.execute(query)
                header = [desc[0] for desc in result.description]
                data = result.fetchall()

        except Exception as e:
            import traceback
            traceback.print_exc()
            print("Error loading extension:", e)
            error_message = str(e) 

        return render(request, 'pbf_viewer/index.html', {'header': header, 
                                                         'data': data, 
                                                         'error_message': error_message,
                                                         'form':form})
