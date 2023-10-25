import json
import os
import xml.etree.ElementTree as ET



def EditFiles(Site, list_id,projectname,Controls, Navigation):
    for root,_,files in os.walk(os.path.dirname(__file__)):
        for file in files:
            fpath = os.path.join(root,file)
            try:
                with open(fpath,'r',encoding='utf-8') as f:
                    text = f.read()
                    f.seek(0)
                    lines = f.readlines()
                if True:
                    if "Forminputs.fx.yaml" == file:
                        change_forminputs(lines,Controls, fpath)
                    if "Solution.xml" == file:
                        change_solution(fpath,text,projectname)
                    if ("Nav" in file or "App" in file) and '.fx.yaml' in file:
                        handle_navigation(Navigation,fpath,text, lines)
                    if "Connections.json" == file:
                        handle_Connections(text,Site,list_id,fpath)
                    if "environmentvariabledefinitions" in fpath and fpath.endswith('.json'):
                        handle_Environment_variables(fpath,text,Site,list_id)
                    if "TableDefinitions" in fpath and "ReportList.json" == file:
                        text = text.replace('7c4a2c8a-ff3c-47bf-bd0c-350283e042b4',list_id).replace('https://greenlandscapingmalmo.sharepoint.com/sites/TrdexperternaApplikationer', Site)
                        with open(fpath,'w',encoding='utf-8') as f:
                            f.write(text)
                if "7c4a2c8a-ff3c-47bf-bd0c-350283e042b4" in text:
                    print(fpath)
                
              
            except:
                import traceback
                #print(traceback.format_exc())
                pass
            
            
            
            
    pass
def handle_Connections(text, Site, list_id, fpath):
    js = json.loads(text)
    js[list(js.keys())[0]]["datasets"] = {
        f"{Site}_al_SharepointSite": {
"datasetOverride": {
"environmentVariableName": "al_SharepointSite"
},
"dataSources": {
"ReportList": {
"tableName": f"{list_id}",
"tableNameOverride": {
"environmentVariableName": "al_ReportList"
}
}}}}
    print(json.dumps(js,indent=2,ensure_ascii=False))
    with open(fpath,'w',encoding='utf-8') as f:
        json.dump(js,f, ensure_ascii=False,indent=2)
                        
def handle_Environment_variables(fpath, text, Site, list_id):
    if "SharepointSite" in fpath and fpath.endswith('.json'):
        js = json.loads(text)
        js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = Site
    elif "ReportList" in fpath and fpath.endswith('.json'):
        js = json.loads(text)
        js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = list_id
        
    with open(fpath,'w',encoding='utf-8') as f:
        json.dump(js,f,ensure_ascii=False,indent=2)
def handle_navigation(Navigation, fpath, text, lines):
    if "App.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if "varNavscreens" in line:
                lines[i] = f"        =Set(varNavscreens,{len([item for item in Navigation if item['value'] != '[[None]]'])});\n"
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    if "Nav1.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav1"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav1"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav2.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav2"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav2"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav3.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav3"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav3"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav4.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav4"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav4"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav5.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav5"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav5"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav6.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav6"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav6"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav7.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav7"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav7"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav8.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav8"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav8"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav9.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav9"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav9"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    elif "Nav10.fx.yaml" in fpath:
        
        for i,line in enumerate(lines):
            if '''        Text: ="Nav10"''' in line:
                lines[i] = f'''        Text: ="{[item["value"] for item in Navigation if item["name"] == f"nav10"][0]}"\n'''
        with open(fpath,'w',encoding='utf-8') as f:
            f.writelines(lines)
    
    


def change_solution(fpath,text, projectname):
    

    root = ET.fromstring(text)
    tag = root.items()
    tag = root.find('SolutionManifest/LocalizedNames/LocalizedName')
    tag.set('description', projectname)
    tag = root.find('SolutionManifest/UniqueName')
    tag.text = projectname

    with open(fpath,'w',encoding='utf-8') as f:
        f.write(ET.tostring(root,encoding='utf-8').decode())


def change_forminputs(textlines, Controls, fpath):
    
    
    target_index=-1
    for j, item in enumerate(Controls):
        if len(textlines) > 600:
            return None
            break
        Moment=item["Moment"]
        Link = item["Link"]
        if Link == "Reng_x00f6_ring_x0020_h_x00e5_rd":
            continue
        lines_to_insert = f"""
        "'{Moment}_DataCard' As typedDataCard.toggleEditCard":
            BorderStyle: =BorderStyle.Solid
            DataField: ="{Link}"
            Default: =ThisItem.{Link}
            DisplayMode: =Parent.DisplayMode
            DisplayName: =DataSourceInfo([@'00TestProjekt Report'],DataSourceInfo.DisplayName,"{Link}")
            Fill: =RGBA(0, 0, 0, 0)
            Height: =50
            Required: =false
            Update: =DataCardValue__{j}.Value
            Visible: =If(Self.DisplayName in ThisItem.Controls.Value,true,false)
            Width: =640
            X: =0
            Y: ={j+1}
            ZIndex: =2

            DataCardKey__{j} As label:
                AutoHeight: =true
                Height: =48
                Size: =21
                Text: =Parent.DisplayName
                Width: =Parent.Width - 60
                Wrap: =false
                X: =30
                Y: =10
                ZIndex: =1

            DataCardValue__{j} As toggleSwitch:
                BorderColor: =If(IsBlank(Parent.Error), Parent.BorderColor, Color.Red)
                Default: =Parent.Default
                DisplayMode: =Parent.DisplayMode
                Height: =31
                Size: =21
                Tooltip: =Parent.DisplayName
                Width: =126
                X: =30
                Y: =DataCardKey__{j}.Y + DataCardKey__{j}.Height + 5
                ZIndex: =2

            ErrorMessage__{j} As label:
                AutoHeight: =true
                Height: =10
                Live: =Live.Assertive
                PaddingBottom: =0
                PaddingLeft: =0
                PaddingRight: =0
                PaddingTop: =0
                Size: =24
                Text: =Parent.Error
                Visible: =Parent.DisplayMode=DisplayMode.Edit
                Width: =Parent.Width - 60
                X: =30
                Y: =DataCardValue__{j}.Y + DataCardValue__{j}.Height
                ZIndex: =3

            StarVisible__{j} As label:
                Align: =Align.Center
                Height: =DataCardKey__{j}.Height
                Size: =21
                Text: ="*"
                Visible: =And(Parent.Required, Parent.DisplayMode=DisplayMode.Edit)
                Width: =30
                Wrap: =false
                Y: =DataCardKey__{j}.Y
                ZIndex: =4
"""
        for i,line in enumerate(textlines):
            if "'Rengöring hårdgjorda ytor_DataCard1' As typedDataCard.toggleEditCard" in line:
                target_index = i 
                break
        if target_index != -1:
            textlines[target_index:target_index] = lines_to_insert
    with open(fpath,'w',encoding='utf-8') as f:
        f.writelines(textlines)
    
                            
if __name__ == '__main__':
    
    
    
    
    Controls=[{
  "Moment": "Äta flugor",
  "Link": "OData__x00c4_ta_x0020_flugor"
},
              {
  "Moment": "Hästtransport",
  "Link": "H_x00e4_sttransport"
},
              {
  "Moment": "Bortforsling av gnuer",
  "Link": "Bortforsling_x0020_av_x0020_gnue"
},
              {
  "Moment": "Leta efter maskrosor",
  "Link": "Leta_x0020_efter_x0020_maskrosor"
},
              {
  "Moment": "Rengöring hårdgjorda ytor",
  "Link": "Reng_x00f6_ring_x0020_h_x00e5_rd"
}]
    
    # Navigation = [{"name":"nav1","value":"Region"},{"name":"nav2","value":"Round"},{"name":"nav3","value":"Savanntyp"},{"name":"nav4","value":"City"},{"name":"nav5","value":"[[None]]"},{"name":"nav6","value":"[[None]]"},{"name":"nav7","value":"[[None]]"},{"name":"nav8","value":"[[None]]"},{"name":"nav9","value":"[[None]]"},{"name":"nav10","value":"[[None]]"}]
    # EditFiles("https://greenlandscapingmalmo.sharepoint.com/sites/TrdexperternaApplikationer","bb01f731-6aa5-47cc-9c38-9dd624fbc105","Egenkontroller_v4", Controls, Navigation)
    import sys
    import base64
    js = json.loads(base64.b64decode(sys.argv[2]).decode())
    if isinstance(js,str):
        js=json.loads(js)
    print(js)
    print(type(js))
    EditFiles(js["Site"],js["ReportListID"],js["ProjectName"],js["Controls"],js["Navigation"])




