import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {

  input: any;

  constructor(private service: SharedService) { }

  ngOnInit(): void {
    this.input = {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      password: ''
    };
  }

  register(): void {
    console.log(this.input);
  }

}
