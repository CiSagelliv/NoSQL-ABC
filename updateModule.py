"""
    actCampos crea/retorna un diccionario con todos los valores de la base de datos
"""
def actCampos():
	return {
	#"_id":self._id,
	"country":country,
	"year":year,
	"sex":sex,
	"age":age,
	"suicides_no":suicides,
	"population":population,
	"suicides/100k pop":suicides_100k_pop,
	"country-year":country_year,
	"HDI for year":HDI_for_year,
	"gdp_for_year($)":gdp_for_year,
	"gdp_per_capita($)":gdp_per_capita,
	"generation":generation
}

"""
    updateCollecion recibe como argumentos el id de la base de datos y actCampos, dentro del método actualiza los campos del diccionario 
    sin contar el id de los datos
"""

def updateCollection(id,**actCampos):
	db=get_db()
	resultado = db.rates.update_one(
		{
           "_id":id          
		}, {
		   '$set': actCampos
		})
	return resultado.modified_count
