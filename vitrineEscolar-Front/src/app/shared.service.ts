import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000"
selectedSchool: any;
//readonly PhotoUrl = "http://127.0.0.1:8000/media"

  constructor(private http:HttpClient) { }

  getEscolaList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + "/api/escola/");
  }

  registerUser(userdata: any):Observable<any>{
    return this.http.post(this.APIUrl + "/api/user/", userdata);
  }

  loginUser(userdata: any):Observable<any>{
    return this.http.post(this.APIUrl + "/api/auth/user", userdata);
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
