import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import '@angular/compiler';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RadioListComponent } from './components/radio-list/radio-list.component';
import {RadioRepository} from './Repositories/RadioRepository';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    RadioListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [RadioRepository],
  bootstrap: [AppComponent]
})
export class AppModule { }
