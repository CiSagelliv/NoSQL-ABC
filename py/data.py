class SuicideRates:
    """
        Aquí irán todos los modulos del programa
    """
    def __init__(self):
        pass
    
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
           "generation":self.generation,
    }