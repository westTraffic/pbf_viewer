from django import forms

class PbfViewerForm(forms.Form):

    ###
    ### Select fields
    ###
    highway = forms.BooleanField(label='Highway', 
                                 initial=False, 
                                 required=False,
                                 widget=forms.CheckboxInput(
                                     attrs={'class': 'form-check-input select_query'}
                                     ))
    maxspeed = forms.BooleanField(label='Max Speed', 
                                  initial=False, 
                                  required=False,
                                  widget=forms.CheckboxInput(
                                      attrs={'class': 'form-check-input select_query'}
                                      ))
    lane = forms.BooleanField(label='Lane', 
                              required=False,
                              widget=forms.CheckboxInput(
                                  attrs={'class': 'form-check-input select_query'}
                                  ))
    oneway = forms.BooleanField(label='Oneway', 
                                required=False,
                                widget=forms.CheckboxInput(
                                    attrs={'class': 'form-check-input select_query'}
                                    ))
    license = forms.BooleanField(label='License', 
                                 required=False,
                                 widget=forms.CheckboxInput(
                                     attrs={'class': 'form-check-input select_query'}
                                     ))
    
    select_other = forms.CharField(label='Amenity', 
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={'id':'select_others',
                                              'class': 'form-control', 
                                              'style': 'width: 100%;',
                                              'placeholder':'Add fields manually'}))
    
    ###
    ### Conditions
    ###
    
    COND_TYPE_CHOICES = [
        ('all', 'All'),
        ('node', 'Node'),
        ('way', 'Way'),
    ]
    cond_type = forms.ChoiceField(label='Type', 
                                  choices=COND_TYPE_CHOICES, 
                                  initial='all',
                                  widget=forms.RadioSelect(
                                      attrs={'class': 'where_rdo_query'}))
    
    COND_ONEWAY_CHOICES = [
        ('all', 'All'),
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    cond_oneway = forms.ChoiceField(label='ONeWay', 
                                  choices=COND_ONEWAY_CHOICES, 
                                  initial='all',
                                  widget=forms.RadioSelect(
                                      attrs={'class': 'where_rdo_query'}))
    cond_amenity = forms.CharField(label='Amenity', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))

    cond_brand = forms.CharField(label='Brand', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))
    cond_state = forms.CharField(label='State', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))
    cond_city = forms.CharField(label='City', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))
    cond_street = forms.CharField(label='Street', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))
    cond_housenumber = forms.CharField(label='HouseNumber', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))
    cond_postcode = forms.CharField(label='PostCode', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control where_txt_query'}))
    
    cond_others = forms.CharField(label='Other', 
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={'id':'select_others',
                                              'class': 'form-control where_txt_query', 
                                              'placeholder':"don't include 'where'"}))
    
    cond_limit = forms.IntegerField(label='Limit', 
                                    min_value=1, 
                                    initial=10,
                                    widget=forms.NumberInput(
                                        attrs={'class': 'form-control'}))
    

    select_sql = forms.CharField(label='SelectSQL', 
                                 required=True,                                
                                 widget=forms.TextInput(
                                     attrs={'id':'select_sql',
                                            'class': 'form-control'}))
    from_sql = forms.CharField(label='FromSQL', 
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={'id':'from_sql',
                                            'placeholder': 'absolute pbf file path',
                                            'class': 'form-control'}))
    
    where_sql = forms.CharField(label='WhereSQL', 
                                 required=False,
                                 widget=forms.TextInput(
                                     attrs={'id':'where_sql',
                                            'class': 'form-control'}))