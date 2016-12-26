# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 18:01:37 2016

@author: joaquin
"""

import urllib2
import csv

class especie:
    
    def __init__ (self, nombre, url):
        
        self.nombre = nombre[:];
        
        downloaded_data  = urllib2.urlopen(url);
        
        historicos = csv.DictReader(downloaded_data);
        
        self.fecha = [];
        self.apertura = [];
        self.maximo = [];
        self.minimo = [];
        self.cierre = [];
        self.volumen = [];
        self.media = [];
        
        for dia in historicos:
            self.fecha.append(dia['fecha'])
            self.apertura.append( float(dia['apertura']));
            self.maximo.append( float(dia['maximo']));
            self.minimo.append( float(dia['minimo']));
            self.cierre.append( float(dia['cierre']));
            self.volumen.append( float(dia['volumen']));
            self.media.append( (float(dia['apertura']) + float(dia['cierre']))/2.0 );
            
        downloaded_data.close()
        
    def getName(self):
        return self.nombre;
        
    def getFecha(self, ultimos_dias = 0):
        '''
        Devuelve las fechas de los ultimos_dias. El default es toda la lista completa
        '''
        return self.fecha[-ultimos_dias : ];
    
    def getApertura(self, ultimos_dias = 0):
        '''
        Devuelve las aperturas de los ultimos_dias. El default es toda la lista completa
        '''
        return self.apertura[-ultimos_dias : ];
        
    def getMaximo(self, ultimos_dias = 0):
        '''
        Devuelve los maximos de los ultimos_dias. El default es toda la lista completa
        '''
        return self.maximo[-ultimos_dias : ];
    
    def getMinimo(self, ultimos_dias = 0):
        '''
        Devuelve los minimos de los ultimos_dias. El default es toda la lista completa
        '''
        return self.minimo[-ultimos_dias : ];
    
    def getCierre(self, ultimos_dias = 0):
        '''
        Devuelve los cierres de los ultimos_dias. El default es toda la lista completa
        '''
        return self.cierre[-ultimos_dias : ];
    
    def getVolumen(self, ultimos_dias = 0):
        '''
        Devuelve los volumenes de los ultimos_dias. El default es toda la lista completa
        '''
        return self.volumen[-ultimos_dias : ];
    
        