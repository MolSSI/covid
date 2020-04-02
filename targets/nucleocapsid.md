# Target: Nucleocapsid Protein

<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/jstree/3.3.8/themes/default/style.min.css" />
<script src="//cdnjs.cloudflare.com/ajax/libs/jstree/3.3.8/jstree.min.js"></script>

<form id="tree_search">
    <input type="search" id="search_querry" />
    <button type="submit">Search</button>
</form>

<table>
	<tr>
		<th>Description</th>
		<th>Orign</th>
		<th>Structural Data</th>
		<th>Simulation Ready Models</th>
		<th>Simulation Input Files</th>
		<th>Trajectories</th>
		<th>Algorithms</th>
		<th>Citations</th>
 	</tr>
{% for member in site.data.nucleocapsid %}
    <tr>
        <td>{{ member.desc }} </td>
        <td>{{ member.origin }} </td>
        <td><span id="struct_data_{{ member.id }}" /></td>
        <td><span id="models_{{ member.id }}"/></td>
        <td><span id="inputs_{{ member.id }}"/></td>
        <td><span id="traj_{{ member.id }}"/></td>
        <td><span id="algo_{{ member.id }}"/></td>
        <td><span id="cite_{{ member.id }}"/></td>
    </tr>
{% endfor %}
</table>

<script>
$(function() {
{% for member in site.data.nucleocapsid %}

{% if member.struct_data != null %}
  $('#struct_data_{{ member.id }}').jstree({
    "plugins" : ["search"],
    'core' : {
      'data' : [
        { "text" : "Structural Data", 
          "children" : [
    {% for struct_child in member.struct_data %}
        {% if struct_child.link == null %}
            {"text": {{ struct_child.text }} },
        {% else %}
            {"text": "{{ struct_child.text }}", a_attr: { href: "{{ struct_child.link }}" } },
        {% endif %} 
    {% endfor %}
          ]
        }
      ],
      'themes' : {
        'variant' : 'large'
      }
    },
  });
  $("#struct_data_{{ member.id }}").on("click", ".jstree-anchor", function(evt) {
    evt.preventDefault();
    var link = $(evt.target).attr("href");
    if (link !== '#') {
      window.open(link);
    }
   });
{% endif %}
   
   
   
  
{% if member.models != null %}   
  $('#models_{{ member.id }}').jstree({
    "plugins" : ["search"],
    'core' : {
      'data' : [
        { "text" : "Simulation Ready Models", 
          "children" : [
    {% for models_child in member.models %}
        {% if models_child.link == null %}
            {"text": "{{ models_child.text }}" },
        {% else %}
            {"text": "{{ models_child.text }}", a_attr: { href: "{{ models_child.link }}" } },
        {% endif %} 
    {% endfor %}
          ]
        }
      ],
      'themes' : {
        'variant' : 'large'
      }
    },
  });
  $("#models_{{ member.id }}").on("click", ".jstree-anchor", function(evt) {
    evt.preventDefault();
    var link = $(evt.target).attr("href");
    if (link !== '#') {
      window.open(link);
    }
   });
{% endif %}

{% if member.inputs != null %}    
  $('#inputs_{{ member.id }}').jstree({
    "plugins" : ["search"],
    'core' : {
      'data' : [
        { "text" : "Simulation Input Files", 
          "children" : [
    {% for input_child in member.inputs %}
        {% if input_child.link == null %}
            {"text": "{{ input_child.text }}" },
        {% else %}
            {"text": "{{ input_child.text }}", a_attr: { href: "{{ input_child.link }}" } },
        {% endif %} 
    {% endfor %}
          ]
        }
      ],
      'themes' : {
        'variant' : 'large'
      }
    },
  });
  $("#inputs_{{ member.id }}").on("click", ".jstree-anchor", function(evt) {
    evt.preventDefault();
    var link = $(evt.target).attr("href");
    if (link !== '#') {
      window.open(link);
    }
   });
{% endif %}


{% if member.trajectories != null %}      
  $('#traj_{{ member.id }}').jstree({
    "plugins" : ["search"],
    'core' : {
      'data' : [
        { "text" : "Trajectories", 
          "children" : [
    {% for traj_child in member.trajectories %}
        {% if traj_child.link == null %}
            {"text": "{{ traj_child.text }}" },
        {% else %}
            {"text": "{{ traj_child.text }}", a_attr: { href: "{{ traj_child.link }}" } },
        {% endif %} 
    {% endfor %}
          ]
        }
      ],
      'themes' : {
        'variant' : 'large'
      }
    },
  });
  $("#traj_{{ member.id }}").on("click", ".jstree-anchor", function(evt) {
    evt.preventDefault();
    var link = $(evt.target).attr("href");
    if (link !== '#') {
      window.open(link);
    }
   });
{% endif %}

{% if member.algorithms != null %}     
  $('#algo_{{ member.id }}').jstree({
    "plugins" : ["search"],
    'core' : {
      'data' : [
        { "text" : "Algorithms", 
          "children" : [
    {% for algo_child in member.algorithms %}
        {% if algo_child.link == null %}
            {"text": "{{ algo_child.text }}" },
        {% else %}
            {"text": "{{ algo_child.text }}", a_attr: { href: "{{ algo_child.link }}" } },
        {% endif %} 
    {% endfor %}
          ]
        }
      ],
      'themes' : {
        'variant' : 'large'
      }
    },
  });
  $("#algo_{{ member.id }}").on("click", ".jstree-anchor", function(evt) {
    evt.preventDefault();
    var link = $(evt.target).attr("href");
    if (link !== '#') {
      window.open(link);
    }
   });
{% endif %}   

{% if member.cite != null %}  
  $('#cite_{{ member.id }}').jstree({
    "plugins" : ["search"],
    'core' : {
      'data' : [
        { "text" : "Citations", 
          "children" : [
    {% for cite_child in member.cite %}
        {% if cite_child.link == null %}
            {"text": "{{ cite_child.text }}" },
        {% else %}
            {"text": "{{ cite_child.text }}", a_attr: { href: "{{ cite_child.link }}" } },
        {% endif %} 
    {% endfor %}
          ]
        }
      ],
      'themes' : {
        'variant' : 'large'
      }
    },
  });
  $("#cite_{{ member.id }}").on("click", ".jstree-anchor", function(evt) {
    evt.preventDefault();
    var link = $(evt.target).attr("href");
    if (link !== '#') {
      window.open(link);
    }
   }); 
{% endif %}  

{% endfor %}

  $("#tree_search").submit(function(e) {
    e.preventDefault();
{% for member in site.data.nucleocapsid %}
    $("#struct_data_{{ member.id }}").jstree(true).search($("#search_querry").val());
    $("#models_{{ member.id }}").jstree(true).search($("#search_querry").val());
    $("#inputs_{{ member.id }}").jstree(true).search($("#search_querry").val());
    $("#traj_{{ member.id }}").jstree(true).search($("#search_querry").val());
    $("#algo_{{ member.id }}").jstree(true).search($("#search_querry").val());
    $("#cite_{{ member.id }}").jstree(true).search($("#search_querry").val());
{% endfor %}
  });
  
});
</script>