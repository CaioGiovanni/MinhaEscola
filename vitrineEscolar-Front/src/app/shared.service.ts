import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000"
//readonly PhotoUrl = "http://127.0.0.1:8000/media"

  constructor(private http:HttpClient) { }

  getEscolaList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + "/api/escola/");
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
