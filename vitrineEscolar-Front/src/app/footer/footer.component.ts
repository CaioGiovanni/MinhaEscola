import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';

declare var closeForm: any;

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  input: any;
  logged: any;
  account: any;

  constructor(private service: SharedService) { }

  ngOnInit(): void {
    this.input = {
      username: '',
      password: ''
    };
    this.logged = false;
    if (localStorage.getItem('Access key') !== null){
      this.logged = true;
    }
  }

  CallCloseForm() {
    closeForm();
  }

  login(): void {
    this.service.loginUser(this.input).subscribe(
      response => {
        console.log(response);
        closeForm();
        localStorage.setItem("Access key", response.access);
        localStorage.setItem("refresh key", response.refresh);
        alert('Usuário ' + this.input.username + ' logado.');
        this.logged = true;
      },
      error => {
        console.log('error', error);
        alert("Não foi possível realizar o login.");
      }
    )
  }

  disconnect(): void {
    localStorage.clear();
    this.logged = false;
  }
}
