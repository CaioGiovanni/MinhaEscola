import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://caire.pythonanywhere.com/api/"
selectedSchool: any;
//readonly PhotoUrl = "http://127.0.0.1:8000/media"

  constructor(private http:HttpClient) { }

  getEscolaList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + "escola/");
  }

  getEscola(pk: string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + "escola/ler/" + pk + "/");
  }

  registerUser(userdata: any):Observable<any>{
    return this.http.post(this.APIUrl + "usuario/criar/", userdata);
  }

  loginUser(userdata: any):Observable<any>{
    return this.http.post(this.APIUrl + "token/", userdata);
  }

  getAvaliacoes(escola: string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + "escola/ler/" + escola);
  }

  postAvaliacao(userdata: any):Observable<any>{
    var reqHeader = new HttpHeaders({ 
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + localStorage.getItem('Access key')
   });
    return this.http.post(this.APIUrl + "avaliacoes/criar/", userdata, { headers: reqHeader });
  }

  getUsuario():Observable<any>{
    var reqHeader = new HttpHeaders({ 
      //'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + localStorage.getItem('Access key')
   });
    return this.http.get<any[]>(this.APIUrl + "usuario/ler/", { headers: reqHeader })
  }

  refreshKey():Observable<any>{
    return this.http.post(this.APIUrl + "token/refresh/", {refresh: localStorage.getItem('refresh key')});
  }
  /*addEscola(val:any){
    return this.http.post<any[]>(this.APIUrl + "/api/escola/", val);
  }

  updateEscola(val:any){
    return this.http.put<any[]>(this.APIUrl + "/api/escola/", val);
  }

  deleteEscola(val:any){
    return this.http.delete<any[]>(this.APIUrl + "/api/escola/", val);
  }*/
}
