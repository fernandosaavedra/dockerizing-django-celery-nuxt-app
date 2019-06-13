<template>
  <div>
    <br/>
    <h2>
      {{title}} &nbsp;&nbsp;
      <small>
        <nuxt-link to="/">Volver</nuxt-link>
      </small>
    </h2>
    <br/><br/>
    <div class="card">
      <header>
        <chartjs-line
          v-bind:backgroundcolor="bgColor"
          v-bind:beginzero="beginZero"
          v-bind:bind="true"
          v-bind:bordercolor="borderColor"
          v-bind:data="data[radio]"
          v-bind:datalabel="dataLabel"
          v-bind:labels="labels[radio]"
        />
      </header>
      <br/><br/>
      <footer class="flex two">
        <label>
          <input v-model="radio" v-bind:name="dataLabel" type="radio" value="v_2018">
          <span class="checkable">Valor 2018</span>
        </label>&nbsp;&nbsp;&nbsp;
        <label>
          <input v-model="radio" v-bind:name="dataLabel" type="radio" value="y_2018">
          <span class="checkable">Variación 2018</span>
        </label><br/>
        <label>
          <input v-model="radio" v-bind:name="dataLabel" type="radio" value="v_2019">
          <span class="checkable">Valor 2019</span>
        </label>&nbsp;&nbsp;&nbsp;
        <label>
          <input v-model="radio" v-bind:name="dataLabel" type="radio" value="y_2019">
          <span class="checkable">Variación 2019</span>
        </label>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      title: 'Gráficos de Variación y Valor del Dolar para 2018 y 2019',
      beginZero: false,
      bgColor: "#771756",
      borderColor: "#771756",
      data: {
        y_2018: [],
        y_2019: [],
        v_2018: [],
        v_2019: []
      },
      dataLabel: "Valor / Variación",
      labels: {
        y_2018: [],
        y_2019: [],
        v_2018: [],
        v_2019: []
},
      radio: "v_2018"
    };
  },
  async created(){
    try{
      const res = await axios.get("http://localhost:8000/dolar/");
      for (var i = 0; i < res.data.length; i++) {
        if(res.data[i].date >= '2018-01-01' && res.data[i].date < '2019-01-01'){
          this.data.y_2018.push(res.data[i].delta);
          this.labels.y_2018.push(res.data[i].date);
          this.data.v_2018.push(res.data[i].val);
          this.labels.v_2018.push(res.data[i].date);
        }else if(res.data[i].date >= '2019-01-01' && res.data[i].date < '2020-01-01'){
          this.data.y_2019.push(res.data[i].delta);
          this.labels.y_2019.push(res.data[i].date);
          this.data.v_2019.push(res.data[i].val);
          this.labels.v_2019.push(res.data[i].date);
        }
      }
    } catch(error){
        console.log(error);
    }
  }
};
</script>