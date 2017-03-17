//export pays=Côte d'Ivoire
create (c:Country {country: {pays}});
create constraint on (o:Country) assert o.country is unique;
