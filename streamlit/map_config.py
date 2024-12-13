location_config = {"version":"v1","config":{"visState":{"filters":[],"layers":[{"id":"jxyxcj","type":"point","config":{"dataId":"Fires","columnMode":"points","label":"point","color":[223, 117, 78],"highlightColor":[252,242,26,255],"columns":{"lat":"Latitude","lng":"Longitude"},"isVisible":True,"visConfig":{"radius":24.7,"fixedRadius":False,"opacity":0.8,"outline":False,"thickness":2,"strokeColor":None,"colorRange":{"name":"Global Warming","type":"sequential","category":"Uber","colors":["#4C0035","#880030","#B72F15","#D6610A","#EF9100","#FFC300"]},"strokeColorRange":{"name":"Global Warming","type":"sequential","category":"Uber","colors":["#4C0035","#880030","#B72F15","#D6610A","#EF9100","#FFC300"]},"radiusRange":[0,50],"filled":True,"billboard":False,"allowHover":True,"showNeighborOnHover":False,"showHighlightColor":True},"hidden":False,"textLabel":[{"field":None,"color":[255,255,255],"size":18,"offset":[0,0],"anchor":"start","alignment":"center","outlineWidth":0,"outlineColor":[255,0,0,255],"background":False,"backgroundColor":[0,0,200,255]}]},"visualChannels":{"colorField":None,"colorScale":"quantile","strokeColorField":None,"strokeColorScale":"quantile","sizeField":None,"sizeScale":"linear"}}],"effects":[],"interactionConfig":{"tooltip":{"fieldsToShow":{"Fires":[{"name":"Temperature_2m","format":None},{"name":"Relative_Humidity_2m","format":None},{"name":"Surface_Pressure","format":None},{"name":"Rain","format":None}]},"compareMode":False,"compareType":"absolute","enabled":True},"brush":{"size":0.5,"enabled":False},"geocoder":{"enabled":False},"coordinate":{"enabled":False}},"layerBlending":"normal","overlayBlending":"normal","splitMaps":[],"animationConfig":{"currentTime":None,"speed":1},"editor":{"features":[],"visible":True}},"mapState":{"bearing":0,"dragRotate":False,"latitude":-17.074457071925416,"longitude":-60.7692710503723,"pitch":0,"zoom":2.8,"isSplit":False,"isViewportSynced":True,"isZoomLocked":False,"splitMapViewports":[]},"mapStyle":{"styleType":"dark","topLayerGroups":{},"visibleLayerGroups":{"label":True,"road":False,"border":True,"building":False,"water":True,"land":True,"3d building":False},"threeDBuildingColor":[15.035172933000911,15.035172933000911,15.035172933000911],"backgroundColor":[0,0,0],"mapStyles":{}}}}

temperature_config = {"version":"v1","config":{"visState":{"filters":[],"layers":[{"id":"jxyxcj","type":"point","config":{"dataId":"Fires","columnMode":"points","label":"point","color":[21,174,180],"highlightColor":[252,242,26,255],"columns":{"lat":"Latitude","lng":"Longitude"},"isVisible":True,"visConfig":{"radius":24.7,"fixedRadius":False,"opacity":0.8,"outline":False,"thickness":2,"strokeColor":None,"colorRange":{"name":"Uber Viz Diverging","type":"diverging","category":"Uber","colors":["#00939C","#6BB5B9","#AAD7D9","#F4B198","#DF744E","#C22E00"]},"strokeColorRange":{"name":"Global Warming","type":"sequential","category":"Uber","colors":["#4C0035","#880030","#B72F15","#D6610A","#EF9100","#FFC300"]},"radiusRange":[0,50],"filled":True,"billboard":False,"allowHover":True,"showNeighborOnHover":False,"showHighlightColor":True},"hidden":False,"textLabel":[{"field":None,"color":[255,255,255],"size":18,"offset":[0,0],"anchor":"start","alignment":"center","outlineWidth":0,"outlineColor":[255,0,0,255],"background":False,"backgroundColor":[0,0,200,255]}]},"visualChannels":{"colorField": {"name": "Temperature_2m","type": "real"},"colorScale":"quantile","strokeColorField":None,"strokeColorScale":"quantile","sizeField":None,"sizeScale":"linear"}}],"effects":[],"interactionConfig":{"tooltip":{"fieldsToShow":{"Fires":[{"name":"Temperature_2m","format":None},{"name":"Relative_Humidity_2m","format":None},{"name":"Surface_Pressure","format":None},{"name":"Rain","format":None}]},"compareMode":False,"compareType":"absolute","enabled":True},"brush":{"size":0.5,"enabled":False},"geocoder":{"enabled":False},"coordinate":{"enabled":False}},"layerBlending":"normal","overlayBlending":"normal","splitMaps":[],"animationConfig":{"currentTime":None,"speed":1},"editor":{"features":[],"visible":True}},"mapState":{"bearing":0,"dragRotate":False,"latitude":-17.074457071925416,"longitude":-60.7692710503723,"pitch":0,"zoom":2.8,"isSplit":False,"isViewportSynced":True,"isZoomLocked":False,"splitMapViewports":[]},"mapStyle":{"styleType":"dark","topLayerGroups":{},"visibleLayerGroups":{"label":True,"road":False,"border":True,"building":False,"water":True,"land":True,"3d building":False},"threeDBuildingColor":[15.035172933000911,15.035172933000911,15.035172933000911],"backgroundColor":[0,0,0],"mapStyles":{}}}}

humidity_config = {"version":"v1","config":{"visState":{"filters":[],"layers":[{"id":"jxyxcj","type":"point","config":{"dataId":"Fires","columnMode":"points","label":"point","color":[21,174,180],"highlightColor":[252,242,26,255],"columns":{"lat":"Latitude","lng":"Longitude"},"isVisible":True,"visConfig":{"radius":24.7,"fixedRadius":False,"opacity":0.8,"outline":False,"thickness":2,"strokeColor":None,"colorRange":{"name":"Uber Viz Diverging","type":"diverging","category":"Uber","colors":["#00939C","#6BB5B9","#AAD7D9","#F4B198","#DF744E","#C22E00"],"reversed": True},"strokeColorRange":{"name":"Global Warming","type":"sequential","category":"Uber","colors":["#4C0035","#880030","#B72F15","#D6610A","#EF9100","#FFC300"]},"radiusRange":[0,50],"filled":True,"billboard":False,"allowHover":True,"showNeighborOnHover":False,"showHighlightColor":True},"hidden":False,"textLabel":[{"field":None,"color":[255,255,255],"size":18,"offset":[0,0],"anchor":"start","alignment":"center","outlineWidth":0,"outlineColor":[255,0,0,255],"background":False,"backgroundColor":[0,0,200,255]}]},"visualChannels":{"colorField": {"name": "Relative_Humidity_2m","type": "real"},"colorScale":"quantile","strokeColorField":None,"strokeColorScale":"quantile","sizeField":None,"sizeScale":"linear"}}],"effects":[],"interactionConfig":{"tooltip":{"fieldsToShow":{"Fires":[{"name":"Temperature_2m","format":None},{"name":"Relative_Humidity_2m","format":None},{"name":"Surface_Pressure","format":None},{"name":"Rain","format":None}]},"compareMode":False,"compareType":"absolute","enabled":True},"brush":{"size":0.5,"enabled":False},"geocoder":{"enabled":False},"coordinate":{"enabled":False}},"layerBlending":"normal","overlayBlending":"normal","splitMaps":[],"animationConfig":{"currentTime":None,"speed":1},"editor":{"features":[],"visible":True}},"mapState":{"bearing":0,"dragRotate":False,"latitude":-17.074457071925416,"longitude":-60.7692710503723,"pitch":0,"zoom":2.8,"isSplit":False,"isViewportSynced":True,"isZoomLocked":False,"splitMapViewports":[]},"mapStyle":{"styleType":"dark","topLayerGroups":{},"visibleLayerGroups":{"label":True,"road":False,"border":True,"building":True,"water":True,"land":True,"3d building":False},"threeDBuildingColor":[15.035172933000911,15.035172933000911,15.035172933000911],"backgroundColor":[0,0,0],"mapStyles":{}}}}

rain_config = {"version":"v1","config":{"visState":{"filters":[],"layers":[{"id":"jxyxcj","type":"point","config":{"dataId":"Fires","columnMode":"points","label":"point","color":[21,174,180],"highlightColor":[252,242,26,255],"columns":{"lat":"Latitude","lng":"Longitude"},"isVisible":True,"visConfig":{"radius":24.7,"fixedRadius":False,"opacity":0.8,"outline":False,"thickness":2,"strokeColor":None,"colorRange":{"name":"Uber Viz Diverging","type":"diverging","category":"Uber","colors":["#00939C","#6BB5B9","#AAD7D9","#F4B198","#DF744E","#C22E00"],"reversed": True},"strokeColorRange":{"name":"Global Warming","type":"sequential","category":"Uber","colors":["#4C0035","#880030","#B72F15","#D6610A","#EF9100","#FFC300"]},"radiusRange":[0,50],"filled":True,"billboard":False,"allowHover":True,"showNeighborOnHover":False,"showHighlightColor":True},"hidden":False,"textLabel":[{"field":None,"color":[255,255,255],"size":18,"offset":[0,0],"anchor":"start","alignment":"center","outlineWidth":0,"outlineColor":[255,0,0,255],"background":False,"backgroundColor":[0,0,200,255]}]},"visualChannels":{"colorField": {"name": "Rain","type": "real"},"colorScale":"quantile","strokeColorField":None,"strokeColorScale":"quantile","sizeField":None,"sizeScale":"linear"}}],"effects":[],"interactionConfig":{"tooltip":{"fieldsToShow":{"Fires":[{"name":"Temperature_2m","format":None},{"name":"Relative_Humidity_2m","format":None},{"name":"Surface_Pressure","format":None},{"name":"Rain","format":None}]},"compareMode":False,"compareType":"absolute","enabled":True},"brush":{"size":0.5,"enabled":False},"geocoder":{"enabled":False},"coordinate":{"enabled":False}},"layerBlending":"normal","overlayBlending":"normal","splitMaps":[],"animationConfig":{"currentTime":None,"speed":1},"editor":{"features":[],"visible":True}},"mapState":{"bearing":0,"dragRotate":False,"latitude":-17.074457071925416,"longitude":-60.7692710503723,"pitch":0,"zoom":2.8,"isSplit":False,"isViewportSynced":True,"isZoomLocked":False,"splitMapViewports":[]},"mapStyle":{"styleType":"dark","topLayerGroups":{},"visibleLayerGroups":{"label":True,"road":False,"border":True,"building":False,"water":True,"land":True,"3d building":False},"threeDBuildingColor":[15.035172933000911,15.035172933000911,15.035172933000911],"backgroundColor":[0,0,0],"mapStyles":{}}}}