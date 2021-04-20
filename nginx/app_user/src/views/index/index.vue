<template>
  <div class="hiric">
    <Navbar />

    <div v-scroll-spy>
      <!--START HOME-->
      <section
        id="home"
        class="home-padding-t-150 position-relative"
        :style="{'background-image': 'url(' + require('@/assets/images/bg-home.jpg') + ')', 'background-size': 'cover','background-position': 'center' }"
      >
        <div class="bg-overlay" />
        <div class="container">
          <div class="row">
            <div class="col-lg-8 offset-lg-2 text-white text-center">
              <h4 class="home-small-title">Data Assets</h4>
              <h1 class="home-title">数据资产估值平台</h1>
              <p
                class="padding-t-15 home-desc mx-auto"
              >未来数据将成为一个重要的财富创造来源，并且越来越多地被视为一项值得重视的企业资产。数据资产的评估问题，也将成为企业估值的核心问题之一。</p>
              <router-link to="/dashboard">
                <button type="button" class="btn btn-custom margin-t-20">开始评估</button>
              </router-link>
              <img src="@/assets/images/home-dashboard.png" alt class="img-fluid margin-t-20">
            </div>
          </div>
        </div>
      </section>
      <!--END HOME-->
      <section class="section-sm bg-light">
        <div class="container">
          <div class="row">
            <div class="col-md-3">
              <div class="client-images my-3 my-md-0">
                <img
                  src="@/assets/images/clients/python-c.png"
                  alt="logo-img"
                  class="mx-auto img-fluid d-block"
                >
              </div>
            </div>

            <div class="col-md-3">
              <div class="client-images my-3 my-md-0">
                <img
                  src="@/assets/images/clients/flask-c.png"
                  alt="logo-img"
                  class="mx-auto img-fluid d-block"
                >
              </div>
            </div>

            <div class="col-md-3">
              <div class="client-images my-3 my-md-0">
                <img
                  src="@/assets/images/clients/vue-c.png"
                  alt="logo-img"
                  class="mx-auto img-fluid d-block"
                >
              </div>
            </div>

            <div class="col-md-3">
              <div class="client-images my-3 my-md-0">
                <img
                  src="@/assets/images/clients/element-c.png"
                  alt="logo-img"
                  class="mx-auto img-fluid d-block"
                >
              </div>
            </div>
          </div>
        </div>
      </section>

      <Features />
      <Footer />
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Features from './components/Features'
import Footer from './components/Footer'

export default {
  components: {
    Navbar,
    Features,
    Footer
  }
}
</script>

<style scoped>
@import "~@/styles/hiric/css/hiric.css";
</style>
