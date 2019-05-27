"""
    actCampos crea/retorna un diccionario con todos los valores de la base de datos
"""
    def actCampos(self):
	    return {
	       #"_id":self._id,
	       "country":self.country,
	       "year":self.year,
	       "sex":self.sex,
	       "age":self.age,
	       "suicides_no":self.suicides,
	       "population":self.population,
	       "suicides/100k pop":self.suicides_100k_pop,
	       "country-year":self.country_year,
	       "HDI for year":self.HDI_for_year,
	       "gdp_for_year($)":self.gdp_for_year,
	       "gdp_per_capita($)":self.gdp_per_capita,
	       "generation":self.generation
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
