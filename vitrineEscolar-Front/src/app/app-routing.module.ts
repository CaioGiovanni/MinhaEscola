import { BuscaComponent } from './views/busca/busca.component';
import { CadastroComponent } from './views/cadastro/cadastro.component';
import { QuemSomosComponent } from './views/quemSomos/quemSomos.component';
import { LoginComponent } from './views/login/login.component';
import { HomeComponent } from './views/home/home.component';
import { PriceComponent } from './views/price/price.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path:'',
    component: HomeComponent
  },
  {
    path:'price',
    component: PriceComponent
  },
  {
    path:'login',
    component: LoginComponent
  },
  {
    path:'cadastro',
    component: CadastroComponent
  },
  {
    path:'busca',
    component: BuscaComponent

  },
  {
    path:'quemSomos',
    component: QuemSomosComponent

  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
