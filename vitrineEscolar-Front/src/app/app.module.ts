import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './views/home/home.component';

import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import { EscolasListComponent } from './views/escolas-list/escolas-list.component';
import {MatTabsModule} from '@angular/material/tabs';
import {MatCardModule} from '@angular/material/card';
import { LoginComponent } from './views/login/login.component';
import { CadastroComponent } from './views/cadastro/cadastro.component';
import { PriceComponent } from './views/price/price.component';
import { QuemSomosComponent } from './views/quemSomos/quemSomos.component';
import { FaqComponent } from './views/faq/faq.component';
import { PreAlfaComponent } from './views/niveisEscolas/preAlfa/preAlfa.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { BuscaComponent } from './views/busca/busca.component';
import { FormcadastroComponent } from './formcadastro/formcadastro.component';
import {SharedService} from './shared.service';

import {APP_BASE_HREF} from '@angular/common';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    EscolasListComponent,
    LoginComponent,
    PriceComponent,
    CadastroComponent,
    QuemSomosComponent,
    PreAlfaComponent,
    NavbarComponent,
    FaqComponent,
    FooterComponent,
    BuscaComponent,
    FormcadastroComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatTabsModule,
    MatCardModule,
    FormsModule, 
    HttpClientModule, 
    ReactiveFormsModule
  ],
  providers: [{provide: APP_BASE_HREF, useValue : '/' }],
  bootstrap: [AppComponent]
})
export class AppModule { }
