    var json = {{ data|tojson }};
    var values = Object.values(json)
    var keys = Object.keys(json)
    console.log(keys.length);
    var canvas = d3.select("body").append("svg").attr("width",100*keys.length).attr("height",500);
    var max = d3.max(values)
    var heightScale = d3.scale.linear().domain([0,max]).range([0,460]);
    var yScale = d3.scale.linear().domain([0,max]).range([480,20]);
    var xScale = d3.scale.ordinal().domain(keys).rangeRoundBands([70, 5000], 0.05);
    var axis = d3.svg.axis().ticks(5).scale(yScale).orient("left");
    var labels = d3.svg.axis().ticks(values.length).scale(xScale).orient("bottom")
    var colorScale = d3.scale.linear().domain([0,max]).range(["white","blue"]);
    var bars = canvas.selectAll("rect").data(values).enter().append("g").attr("transform",function(v,i){return "translate("+xScale(keys[i])+","+(480-heightScale(v))+")"});
    bars.append("rect").attr("height", function(i){return heightScale(i)}).attr("width",xScale.rangeBand())
    .attr("fill", function(i){return colorScale(10000000)});
    bars.append("text").text(function(d,i){return d}).attr("z",1).attr("y",15).attr("opacity",0.2);
    bars.on("mouseover", function(d){d3.select(this).select("rect").attr("fill","red");d3.select(this).select("text").attr("opacity",1.0)})
    .on("mouseout", function(d){d3.select(this).select("rect").attr("fill","blue");d3.select(this).select("text").attr("opacity",0.2)})
    .on("click", function(d){alert(d)})
    canvas.append("g").attr("transform","translate(70,0)").call(axis)
    canvas.append("g").attr("transform","translate(0,480)").call(labels)
