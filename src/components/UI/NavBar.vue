<template>
  <nav class="nav">

    <div class="nav__block">
      <img class="sidebar" src="../../assets/sidebar.png" alt="" >
      <img @click="this.$router.push('/')" class="logo" src="../../assets/logo.png" alt="">
      <div class="nav__link">Студенты</div>
      <div @click="this.$router.push('/posts')" class="nav__link">Проекты</div>
      <div class="nav__link">Биржа</div>
      <a class="nav__link" href="http://127.0.0.1:8001/admin/">Админка</a>
    </div>

    <div class="nav__block">
      <img class="logo" src="../../assets/logoEnter.png" alt="">
      <div class="name">
        Школенко <p/>
        Кирилл
      </div>
    </div>

  </nav>
</template>

<script>
export default {
  name: 'my-navbar',
}
</script>

<style scoped>
.nav{
  display: flex;
  justify-content: space-between;


}
.sidebar{
  padding: 10px;
}
.logo{
  padding: 15px;
}
.name{
  color: white;
  padding: 15px;
}

.nav__block{
  display: flex;
  align-items: center;
}
.nav__link{
  font-size: 20px;
  color: white;
  padding: 15px;
  display: inline-block;
}
</style>