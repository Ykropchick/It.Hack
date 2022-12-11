<template>
  <div class="container">
    <div class="row">
      <div class="row justify-content-center Digital text">
        ЦИФРОВАЯ ПЛАТФОРМА
      </div>
      <div class="row justify-content-center Itmo text">
        ИТМО х ПИШ
      </div>
    </div>
    <div class="row blockWhat">
      <div class="col text forWhom">
        Что это
        и для кого?
      </div>
      <div class="col text Descriptions">
        ЦИФРОВАЯ ПЛАТФОРМА - новый проект передовой инженерной школы Университета ИТМО, нацеленный на построение профессиональных связей между студентамии крупными российскими компаниями;
      </div>
    </div>

    <div class="row block">
      <div class="row block__title justify-content-center">
        Для студентов
      </div>
      <div class="row student mt-5">

        <div class="col post">
          <div class="row title">
            Реальные проекты от ведущих компаний
          </div>
          <div class="row body">
            Примите участие в разработке нового продукта или решите производственную задачу совместно с партнерами платформы
          </div>
        </div>

        <div class="col post ">
          <div class="row title">
            Стажировкии трудоустройство
          </div>
          <div class="row body">
            По результатам проделанной работы, получите возможность пройти учебную стажировку или стать новым сотрудником компании
          </div>
        </div>

        <div class="col post m-auto">
          <div class="row title">
            Реализация своих разработок
          </div>
          <div class="row body">
            Продвигайте собственные научные идеи, расскажите о своем стартапеи привлекайте внимание и инвестиции с помощью биржи.
          </div>
        </div>
        <div class="row justify-content-center ButtonDiv">
          <button type="button" class="btn btn-primary ButtonMore">Подробнее</button>
        </div>
      </div>
    </div>

    <div class="row block">
      <div class="row block__title justify-content-center">
        Для компаний
      </div>
      <div class="row student mt-5">

        <div class="col post">
          <div class="row title">
            Реальные проекты от ведущих компаний
          </div>
          <div class="row body">
            Перспективные студенты ИТМО и ПИШ - новые таланты и ваши будущие сотрудники
          </div>
        </div>

        <div class="col post ">
          <div class="row title">
            Найдите исполнителей
          </div>
          <div class="row body">
            Решением вашей производственной задачи займутся команды студентов из ведущего вуза страны
          </div>
        </div>

        <div class="col post m-auto">
          <div class="row title">
            Получите доступ к резюме
          </div>
          <div class="row body">
            Партнерам платформы доступна расширенная информация о профессиональных навыках исполнителей
          </div>
        </div>
        <div class="row justify-content-center ButtonDiv">
          <button type="button" class="btn btn-primary ButtonMore">Подробнее</button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "MainPage",



}
</script>


<style scoped>


.Itmo{
  color: white;
}
.Digital{
  color: white;
}

.Digital{

  color: transparent!important;
  -webkit-text-stroke: 2px white;
  font-family: Inter;
  font-style: normal;
  font-weight: 800;
  font-size: 50px;
  line-height: 116px;

}

.Itmo{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 800;
  font-size: 36px;
  line-height: 77px;

}

.text{
  color: white;
}
.forWhom{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 800;
  font-size:  80px;
  line-height: 116px;

}
.Descriptions{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 29px;
  margin-top: 30px;
}
.student{
  color: white;
}
.title{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 800;
  font-size: 24px;
  line-height: 39px;
}
.body{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 800;
  font-size: 15px;
  line-height: 39px;
}
.container{
  margin-top: 150px;
}
.post{
  margin-right: 50px;
}
.block__title{
  color: white;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 800;
  font-size: 50px;
  line-height: 77px;
}
.block{
  background: rgba(34, 17, 131, 0.35);
  backdrop-filter: blur(25px);
  border-radius: 25px;
  padding-top: 100px;

}

.blockWhat{
  margin-top: 300px;
  padding-bottom: 100px;

}
.ButtonMore{
  width: 20%;
  background: linear-gradient(0deg, #7B45EC, #7B45EC), #FFFFFF;
  border-radius: 50px;
}
.ButtonDiv{
  padding-top: 35px;

}
</style>
