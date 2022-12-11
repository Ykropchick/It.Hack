<template>


<div class="container">
  <div class="row w-500">
    <div class="row justify-content-center Digital text">
      ЦИФРОВАЯ ПЛАТФОРМА
    </div>
    <div class="row justify-content-center Itmo text">
      ИТМО х ПИШ
    </div>
  </div>
  <div class="row block">
    <div class="row block__title justify-content-center">
      Вход в аккаунт
    </div>

    <div class="row block__username">
      <input v-model="login" type="text" class="block__username text-center" placeholder="Логин">
    </div>

    <div class="row block__password">
      <input v-model="password" type="password" class="block__password text-center" placeholder="Пароль">
    </div>

    <div class="row justify-content-center">
      <button type="button" class="btn btn-primary block__btn">Войти</button>
    </div>

    <div class="row block__under">

    </div>


  </div>
</div>


</template>

<script>
export default {
  name: "EnterPage",
  data(){
    return{
      login: '',
      password: '',
    }
  }



}
</script>

<style scoped>
.container{
  color: white;
}
.Digital{

  padding-top: 50px;

  color: transparent!important;
  -webkit-text-stroke: 2px white;
  font-family: Inter;
  font-style: normal;
  font-weight: 800;
  font-size: 50px;
  line-height: 116px;

}

.block{
  padding-top: 65px;
}

.Itmo{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 800;
  font-size: 36px;
  line-height: 77px;

}
.block__password{
  margin-top: 20px;
}
.block__username{
  margin-top: 10px;
}
.block__password, .block__username{
  /*width: 70%;*/
  background: rgba(123, 69, 236, 0.5);
  backdrop-filter: blur(25px);
  border-radius: 16px;
  height: 45px;
}
.block__btn{
  margin-top: 40px;
  width: 20%;
  background: #7B45EC;
  /*filter: blur(17.5px);*/
  border-radius: 50px;
}
</style>