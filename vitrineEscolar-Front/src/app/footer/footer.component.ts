import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  input: any;
  logged: any;

  constructor(private service: SharedService) { }

  ngOnInit(): void {
    this.input = {
      username: '',
      password: ''
    };
    this.logged = false;
  }

  login(): void {
    this.service.loginUser(this.input).subscribe(
      response => {
        console.log(response);
        alert('Usuário' + this.input.username + 'logado.');
      },
      error => {
        console.log('error', error);
      }
    )
  }

  disconnect(): void {
    localStorage.clear();
    this.logged = false;
  }
}
