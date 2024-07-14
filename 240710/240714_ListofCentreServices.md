# [14 Jul 2024] List of Centre Services by Early Childhood Development Agency

This project uses the `listing of centre services` from Early Childhood Development Agency (ECDA) to allow users to search for pre-school centres that are within their budget and suitable care timings. 

The data contains duplicate centre names with different centre codes and updated date. In order to prevent duplicated records in our search results, we'll first remove the duplicate after standardising the centre names, service types, class of licence, levels offered and citizenship to titlecase. 

Thereafter, we plot the boxplots to get a sense of the distribution of fees for different level offers, citizenship and type of services in order to setup the selection options within `ipywidgets` in jupyter notebooks. A better approach might be to use Tableau Public which is more user-friendly and has a lower learning curve for normal users. 

Based on the boxplots, we noted that the median fees for Singapore citizens tend to be lower as compared to permanent residents and others. Additionally, full day and flexible services tend to have higher fees as compared to half-day and fixed schedule. This might be due to additional resources and coordination required by the centres. 

Using the code block below, we create an interactive interface for the user to interact and select the relevant options as follows in order to shortlist the potential centre that they can engage for their child(ren). The output is saved as a `csv` file in the folder [output](/240710/output).
- Budget
- Levels offered 
- Type of Service 
- Citizenship

```python 
import ipywidgets as widgets 
from ipywidgets import interactive_output
from IPython.display import display 

max_fees_widget = widgets.IntSlider(value=500, min=0, max=4500, step=20, description='Max. Budget:', continuous_update=False)
levels_widget = widgets.Dropdown(options=df['levels_offered'].unique(), description='Level:', disabled=False)
service_type_widget = widgets.Dropdown(options=df['type_of_service'].unique(), description='Service Type:', disabled=False)
citizenship_widget = widgets.Dropdown(options=df['type_of_citizenship'].unique(), value='Sc', description='Citizenship:', disabled=False)

def show_data(budget, level, service_type, citizenship): 
    filtered_data = df[
        (df['fees'] <= budget) &
        (df['levels_offered'] == level) &
        (df['type_of_service'] == service_type) & 
        (df['type_of_citizenship'] == citizenship)
    ]
    display(filtered_data)
    filtered_data.to_csv(f"output/list_of_centres_{budget}_{service_type}_{level}.csv", index=False)

interactive = interactive_output(show_data, {
    'budget': max_fees_widget,
    'level': levels_widget,
    'service_type': service_type_widget,
    'citizenship': citizenship_widget
})    

display(max_fees_widget, levels_widget, service_type_widget, citizenship_widget, interactive)
```

![Interactive Search of Early Childhood Centres](img/Screenshot%202024-07-14%20at%207.24.55 PM.png)