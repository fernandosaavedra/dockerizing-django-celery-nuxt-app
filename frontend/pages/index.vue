<template>
  <header id="header-inicio">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xs-12"><br/><br/>
          <div id="logo">
            <span class="logo-text">
              <span class="gris">{{name}}</span><span class="purpura">{{last_name}}</span><span class="purpura guion-bajo">_</span>
            </span>
            <span class="slogan">{{tagline}}</span></div>
            <div class="button-container">
              <nuxt-link class="btn btn-info" id="button-start" to="/charts">Ver Gráficos</nuxt-link>
              <a href="#" class="btn btn-info" id="button-project" role="button">Github</a>
            </div>
        </div>
        <div class="clearfix"></div>
      </div>
    </div>
  </header>

</template>

<script>
export default {
  data() {
    return {
      name: 'fernando',
      last_name: 'saavedra',
      tagline: 'Fullstack Developer'
    }
  }
};
</script>

<style lang="scss" scoped>
  #header-inicio{
    position:relative;
    height:100vh;
  }
  .button-container{
    width:100%;
    text-align:center;
    margin-top:40px;
  }
  #button-start{
    display:inline-block;
    padding:15px 25px;
    background:#771756;
    color:white;
    font-family:'Lato',sans-serif;
    font-weight:400;
    text-decoration:none;
  }
  #button-project{
    display:inline-block;
    padding:15px 25px;
    background:#771756;
    color:white;
    font-family:'Lato',sans-serif;
    font-weight:400;
    text-decoration:none;
  }
</style>