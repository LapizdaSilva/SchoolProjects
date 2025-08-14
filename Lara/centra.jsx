import React from 'react';

import { View, Text, StyleSheet } from 'react-native';

export default function App() {
return (
<View style = {estilos.centralizar}>
<Text style = {estilos.texto}>Olá, mundo!</Text>
</View>
);

}

const estilos = StyleSheet.create({
centralizar: {
flex: 1,
justifyContent: 'center',
alignItems: 'center',

},
    texto: {
    color: 'blue',  
    fontSize: 35,
}
});