library(RSelenium)
library(rlang)
library(readr)

#Crea un control remoto
RDrive<-rsDriver()

#Función para la descarga
inegi_inpp_descarga<-function(y_inicial, m_inicial, y_final, m_final)
{
      #############  Abre navegador en INEGI  ###################################
      RDrive1<-RDrive[["client"]]
      RDrive1$open()
      RDrive1$navigate("http://www3.inegi.org.mx/sistemas/inp/preciospromedio/")
      
      Sys.sleep(5)
      
      ############  Seleciona todas las ciudades y todos los productos  ########
      searchIDGeo <-'//*[@id="SerieChBox-01"]'
      webElem<-RDrive1$findElement(value = searchIDGeo)
      webElem$clickElement()
      
      searchIDProd <-'//*[@id="SerieChBox-0"]'
      webElem<-RDrive1$findElement(value = searchIDProd)
      webElem$clickElement()
      
      ###########  Crea las posibles combinaciones mes x año  ##################
      year<-data.frame(y=c("2011","2012","2013","2014","2015","2016","2017"), id=1:7)
      month<-data.frame(m=c("01","02","03","04","05","06","07","08","09","10","11","12"), id=1:12)
      
      year_inicial<-year[year$y==y_inicial,2]
      year_final<-year[year$y==y_final,2]
      
      mes_inicial<-month[month$m==m_inicial,2]
      mes_final<-month[month$m==m_final,2]
      
      ###########  Inicia la descarga mes por mes  #############################
      for(k in year_inicial:year_final)
      { 
            for(j in mes_inicial:mes_final)
            {
                  Sys.sleep(5)
                  ####  Seleciona fecha de inicio de la descarga  ##############
                  searchIDDateI <-'//*[(@id = "PeriodoInicio")]'
                  webElemDateI<-RDrive1$findElement(value = searchIDDateI)
                  webElemDateI$clickElement()
                  webElemDateI$sendKeysToElement(list(paste0(year[k,1],"/",month[j,1]),key="enter"))
                  ####  Seleciona fecha de término de la descarga  #############
                  searchIDDateF <-'//*[(@id = "PeriodoFin")]'
                  webElemDateF<-RDrive1$findElement(value = searchIDDateF)
                  webElemDateF$clickElement()
                  webElemDateF$sendKeysToElement(list(paste0(year[k,1],"/",month[j,1]),key="enter"))
                  ####  Inicio de la descarga  #################################
                  tableIDcsv<-'//*[(@alt = "Consulta las series seleccionadas en formato separado por comas (CSV).")]'
                  webElem2<-RDrive1$findElement(value = tableIDcsv)
                  webElem2$clickElement()
                  
            }
      }
      Sys.sleep(600)
      
      ##########  Cierra el navegador  #########################################
      RDrive1$close()
}

#Función para la carga de los datos y borrado de archivos temporales
inegi_inpp_integra<-function(usuario){
      
      #Idenfica los archivos
      archivos<-list.files(path = paste0("D:/Users/",usuario,"/Downloads"), pattern = "INP_PP2017*.*")
      
      df_archi<-as.data.frame(archivos)
      
      df_inegi_total<-data.frame()
      #Une los archivos y borra los archivos temporales
      for(i in 1:nrow(df_archi)){
            archivo_i<-read_csv(paste0("D:/Users/",usuario,"/Downloads","/",df_archi[i,1]),skip = 5)
            df_inegi_total<-rbind(df_inegi_total,archivo_i)
            file.remove(paste0("D:/Users/",usuario,"/Downloads","/",df_archi[i,1]))
      }
}
